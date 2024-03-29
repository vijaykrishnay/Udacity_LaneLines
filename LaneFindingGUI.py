import wx
import LaneFindingAuto
import os
import cv2
import numpy as np
import glob

def scale_bitmap(bitmap, scale_factor):
    image = wx.ImageFromBitmap(bitmap)
    image_scaled = image.Scale(image.GetWidth()*scale_factor, image.GetHeight()*scale_factor, wx.IMAGE_QUALITY_HIGH)
    return wx.BitmapFromImage(image_scaled)

def set_bitmap_image(wx_bitmap, image, scale=0.5):
    try:
        width, height, nrgb = image.shape
    except ValueError:
        width, height = image.shape
        image = np.dstack([image]*3)

    img_bmp = wx.Bitmap.FromBuffer(height, width, image)
    bmp_scaled = scale_bitmap(img_bmp, scale_factor=scale)
    wx_bitmap.SetBitmap(bmp_scaled)

class LaneFindingMain(LaneFindingAuto.LaneFindingTuning):
    def __init__(self, parent):
        LaneFindingAuto.LaneFindingTuning.__init__(self, parent)
        self.update_dir(None)

    def update_dir(self, event):
        self.dir_path = self.dirPicker.GetPath()
        self.img_files = glob.glob(os.path.join(self.dir_path, '*.jpg'))
        self.counter = 0
        self.update_images(None)
    
    def next_image(self, event):
        self.counter += 1
        if self.counter >= len(self.img_files):
            self.counter = 0
        self.update_images(None)

    def update_images(self, event):
        if not self.img_files:
            return
        
        filepath = self.img_files[self.counter]
        self.staticText_fileName.SetLabel(filepath)

        if not os.path.exists(filepath):
            return
        
        # ORIGINAL IMAGE
        img = cv2.imread(filepath)
        img_gray = cv2.imread(filepath, 0)
        set_bitmap_image(self.bitmap_original, img)

        # GAUSSIAN BLUR
        kernel_size_x = (self.slider_gauss_x.GetValue()*2) + 1
        kernel_size_y = (self.slider_gauss_y.GetValue()*2) + 1
        blur_gray = cv2.GaussianBlur(img_gray, (kernel_size_x, kernel_size_y), 0)
        set_bitmap_image(self.bitmap_gauss, blur_gray)

        # CANNY EGDES
        min_threshold = self.slider_canny_min.GetValue()
        max_threshold = self.slider_canny_max.GetValue()
        edges = cv2.Canny(blur_gray, min_threshold, max_threshold)
        set_bitmap_image(self.bitmap_canny, edges)

        # MASK IMAGE
        h = edges.shape[0]
        w = edges.shape[1]
        x0 = int(float(self.textCtrl_x0.GetValue()) * w)
        x1a = int(float(self.textCtrl_x1a.GetValue()) * w)
        y1a = int(float(self.textCtrl_y1a.GetValue()) * h)
        x1b = int(float(self.textCtrl_x1b.GetValue()) * w)
        y1b = int(float(self.textCtrl_y1b.GetValue()) * h)
        x2 = int(float(self.textCtrl_x2.GetValue()) * w)
        
        vertices = np.array([[(x0, h), (x1a, y1a), (x1b, y1b), (x2, h)]], dtype=np.int32)
        ignore_mask_color = 255
        print(vertices)

        mask = np.zeros_like(edges)
        cv2.fillPoly(mask, vertices, ignore_mask_color)
        masked_edges = cv2.bitwise_and(edges, mask)
        masked_edges_marked = np.dstack((masked_edges, masked_edges, masked_edges))
        cv2.line(masked_edges_marked, (x0, h), (x1a, y1a), (0, 255, 0), 1)
        cv2.line(masked_edges_marked, (x1a, y1a), (x1b, y1b), (0, 255, 0), 1)
        cv2.line(masked_edges_marked, (x1b, y1b), (x2, h), (0, 255, 0), 1)
        set_bitmap_image(self.bitmap_mask, masked_edges_marked)

        # HOUGH LINES
        rho = self.slider_rho.GetValue()
        theta = self.slider_theta.GetValue()/1800.
        threshold = self.slider_threshold.GetValue()
        min_line_len = self.slider_minLineLen.GetValue()
        max_line_gap = self.slider_maxLineGap.GetValue()
        lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]), min_line_len, max_line_gap)

        line_image = np.zeros_like(img)
        # Draw lines on the image
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 3)
        set_bitmap_image(self.bitmap_lines, line_image)

        # FINAL IMAGE
        # # Create a "color" binary image to combine with line image
        # color_edges = np.dstack((edges, edges, edges)) 

        # Draw the lines on the edge image
        combo = cv2.addWeighted(img, 0.8, line_image, 1, 0) 
        set_bitmap_image(self.bitmap_final, combo)
                
        self.mainFrame.Layout()
        self.mainFrame.Refresh()

app = wx.App()   # Error messages go to popup window
top = LaneFindingMain(None)
top.Show()
app.MainLoop()
