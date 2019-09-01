# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class LaneFindingTuning
###########################################################################

class LaneFindingTuning ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.mainFrame = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.mainFrame.SetScrollRate( 5, 5 )
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.dirPicker = wx.DirPickerCtrl( self.mainFrame, wx.ID_ANY, u"test_images", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer9.Add( self.dirPicker, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.staticText_fileName = wx.StaticText( self.mainFrame, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_fileName.Wrap( -1 )
		bSizer10.Add( self.staticText_fileName, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.button_next = wx.Button( self.mainFrame, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.button_next, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.bitmap_original = wx.StaticBitmap( self.mainFrame, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.bitmap_original, 0, wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self.mainFrame, wx.ID_ANY, u"Gaussian Blur", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.slider_gauss_x = wx.Slider( self.mainFrame, wx.ID_ANY, 2, 0, 99, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer4.Add( self.slider_gauss_x, 0, wx.ALL, 5 )
		
		self.slider_gauss_y = wx.Slider( self.mainFrame, wx.ID_ANY, 2, 0, 99, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer4.Add( self.slider_gauss_y, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer4, 0, 0, 5 )
		
		
		fgSizer1.Add( bSizer3, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.bitmap_gauss = wx.StaticBitmap( self.mainFrame, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.bitmap_gauss, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText21 = wx.StaticText( self.mainFrame, wx.ID_ANY, u"Canny Edges", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		bSizer31.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.slider_canny_min = wx.Slider( self.mainFrame, wx.ID_ANY, 50, 1, 999, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer41.Add( self.slider_canny_min, 0, wx.ALL, 5 )
		
		self.slider_canny_max = wx.Slider( self.mainFrame, wx.ID_ANY, 180, 1, 999, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer41.Add( self.slider_canny_max, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( bSizer41, 0, 0, 5 )
		
		
		fgSizer1.Add( bSizer31, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bitmap_canny = wx.StaticBitmap( self.mainFrame, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.bitmap_canny, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer8.Add( fgSizer1, 0, 0, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer311 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText211 = wx.StaticText( self.mainFrame, wx.ID_ANY, u"Mask Vertices \n(Normalized: 0 - 1)", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.m_staticText211.Wrap( -1 )
		self.m_staticText211.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		bSizer311.Add( self.m_staticText211, 0, wx.ALL, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.textCtrl_x0 = wx.TextCtrl( self.mainFrame, wx.ID_ANY, u"0.1", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.textCtrl_x0, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.mainFrame, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.textCtrl_x1a = wx.TextCtrl( self.mainFrame, wx.ID_ANY, u"0.472", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.textCtrl_x1a, 0, wx.ALL, 5 )
		
		self.textCtrl_y1a = wx.TextCtrl( self.mainFrame, wx.ID_ANY, u"0.595", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.textCtrl_y1a, 0, wx.ALL, 5 )
		
		self.textCtrl_x1b = wx.TextCtrl( self.mainFrame, wx.ID_ANY, u"0.528", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.textCtrl_x1b, 0, wx.ALL, 5 )
		
		self.textCtrl_y1b = wx.TextCtrl( self.mainFrame, wx.ID_ANY, u"0.595", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.textCtrl_y1b, 0, wx.ALL, 5 )
		
		self.textCtrl_x2 = wx.TextCtrl( self.mainFrame, wx.ID_ANY, u"0.94", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.textCtrl_x2, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self.mainFrame, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer311.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		fgSizer5.Add( bSizer311, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bitmap_mask = wx.StaticBitmap( self.mainFrame, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.bitmap_mask, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2111 = wx.StaticText( self.mainFrame, wx.ID_ANY, u"Hough Lines", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.m_staticText2111.Wrap( -1 )
		self.m_staticText2111.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		bSizer19.Add( self.m_staticText2111, 0, wx.ALL, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( self.mainFrame, wx.ID_ANY, u"Rho", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		fgSizer4.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.slider_rho = wx.Slider( self.mainFrame, wx.ID_ANY, 1, 1, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		fgSizer4.Add( self.slider_rho, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self.mainFrame, wx.ID_ANY, u"Theta", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		fgSizer4.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.slider_theta = wx.Slider( self.mainFrame, wx.ID_ANY, 28, 1, 1800, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		fgSizer4.Add( self.slider_theta, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self.mainFrame, wx.ID_ANY, u"Threshold", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		fgSizer4.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.slider_threshold = wx.Slider( self.mainFrame, wx.ID_ANY, 20, 1, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		fgSizer4.Add( self.slider_threshold, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.mainFrame, wx.ID_ANY, u"Min. Line Length", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		fgSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.slider_minLineLen = wx.Slider( self.mainFrame, wx.ID_ANY, 45, 1, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		fgSizer4.Add( self.slider_minLineLen, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.mainFrame, wx.ID_ANY, u"Max. Line Gap", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		fgSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.slider_maxLineGap = wx.Slider( self.mainFrame, wx.ID_ANY, 45, 1, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		fgSizer4.Add( self.slider_maxLineGap, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( fgSizer4, 0, 0, 5 )
		
		
		fgSizer5.Add( bSizer19, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.bitmap_lines = wx.StaticBitmap( self.mainFrame, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.bitmap_lines, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.mainFrame, wx.ID_ANY, u"Final Image", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		
		fgSizer5.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bitmap_final = wx.StaticBitmap( self.mainFrame, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.bitmap_final, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( fgSizer5, 0, 0, 5 )
		
		
		self.mainFrame.SetSizer( bSizer8 )
		self.mainFrame.Layout()
		bSizer8.Fit( self.mainFrame )
		bSizer1.Add( self.mainFrame, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.dirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.update_dir )
		self.button_next.Bind( wx.EVT_BUTTON, self.next_image )
		self.slider_gauss_x.Bind( wx.EVT_SCROLL_CHANGED, self.update_images )
		self.slider_gauss_y.Bind( wx.EVT_SCROLL_CHANGED, self.update_images )
		self.slider_canny_min.Bind( wx.EVT_SCROLL_CHANGED, self.update_images )
		self.slider_canny_max.Bind( wx.EVT_SCROLL_CHANGED, self.update_images )
		self.textCtrl_x0.Bind( wx.EVT_TEXT_ENTER, self.update_images )
		self.textCtrl_x1a.Bind( wx.EVT_TEXT_ENTER, self.update_images )
		self.textCtrl_y1a.Bind( wx.EVT_TEXT_ENTER, self.update_images )
		self.textCtrl_x1b.Bind( wx.EVT_TEXT_ENTER, self.update_images )
		self.textCtrl_y1b.Bind( wx.EVT_TEXT_ENTER, self.update_images )
		self.textCtrl_x2.Bind( wx.EVT_TEXT_ENTER, self.update_images )
		self.m_button1.Bind( wx.EVT_BUTTON, self.update_images )
		self.slider_rho.Bind( wx.EVT_SCROLL_CHANGED, self.update_images )
		self.slider_theta.Bind( wx.EVT_SCROLL_CHANGED, self.update_images )
		self.slider_threshold.Bind( wx.EVT_SCROLL_CHANGED, self.update_images )
		self.slider_minLineLen.Bind( wx.EVT_SCROLL_CHANGED, self.update_images )
		self.slider_maxLineGap.Bind( wx.EVT_SCROLL_CHANGED, self.update_images )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def update_dir( self, event ):
		event.Skip()
	
	def next_image( self, event ):
		event.Skip()
	
	def update_images( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

