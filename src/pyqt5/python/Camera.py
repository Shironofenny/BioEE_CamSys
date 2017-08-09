import cv2
import Constant

    # Documentation from OpenCV's github on camera properties. The official documentation is outdated
    # Python interface uses directly the id code
    #   CAP_PROP_POS_MSEC       =0, //!< Current position of the video file in milliseconds.
    #   CAP_PROP_POS_FRAMES     =1, //!< 0-based index of the frame to be decoded/captured next.
    #   CAP_PROP_POS_AVI_RATIO  =2, //!< Relative position of the video file: 0=start of the film, 1=end of the film.
    #   CAP_PROP_FRAME_WIDTH    =3, //!< Width of the frames in the video stream.
    #   CAP_PROP_FRAME_HEIGHT   =4, //!< Height of the frames in the video stream.
    #   CAP_PROP_FPS            =5, //!< Frame rate.
    #   CAP_PROP_FOURCC         =6, //!< 4-character code of codec. see VideoWriter::fourcc .
    #   CAP_PROP_FRAME_COUNT    =7, //!< Number of frames in the video file.
    #   CAP_PROP_FORMAT         =8, //!< Format of the %Mat objects returned by VideoCapture::retrieve().
    #   CAP_PROP_MODE           =9, //!< Backend-specific value indicating the current capture mode.
    #   CAP_PROP_BRIGHTNESS    =10, //!< Brightness of the image (only for those cameras that support).
    #   CAP_PROP_CONTRAST      =11, //!< Contrast of the image (only for cameras).
    #   CAP_PROP_SATURATION    =12, //!< Saturation of the image (only for cameras).
    #   CAP_PROP_HUE           =13, //!< Hue of the image (only for cameras).
    #   CAP_PROP_GAIN          =14, //!< Gain of the image (only for those cameras that support).
    #   CAP_PROP_EXPOSURE      =15, //!< Exposure (only for those cameras that support).
    #   CAP_PROP_CONVERT_RGB   =16, //!< Boolean flags indicating whether images should be converted to RGB.
    #   CAP_PROP_WHITE_BALANCE_BLUE_U =17, //!< Currently unsupported.
    #   CAP_PROP_RECTIFICATION =18, //!< Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently).
    #   CAP_PROP_MONOCHROME    =19,
    #   CAP_PROP_SHARPNESS     =20,
    #   CAP_PROP_AUTO_EXPOSURE =21, //!< DC1394: exposure control done by camera, user can adjust reference level using this feature.
    #   CAP_PROP_GAMMA         =22,
    #   CAP_PROP_TEMPERATURE   =23,
    #   CAP_PROP_TRIGGER       =24,
    #   CAP_PROP_TRIGGER_DELAY =25,
    #   CAP_PROP_WHITE_BALANCE_RED_V =26,
    #   CAP_PROP_ZOOM          =27,
    #   CAP_PROP_FOCUS         =28,
    #   CAP_PROP_GUID          =29,
    #   CAP_PROP_ISO_SPEED     =30,
    #   CAP_PROP_BACKLIGHT     =32,
    #   CAP_PROP_PAN           =33,
    #   CAP_PROP_TILT          =34,
    #   CAP_PROP_ROLL          =35,
    #   CAP_PROP_IRIS          =36,
    #   CAP_PROP_SETTINGS      =37, //!< Pop up video/camera filter dialog (note: only supported by DSHOW backend currently. The property value is ignored)
    #   CAP_PROP_BUFFERSIZE    =38,
    #   CAP_PROP_AUTOFOCUS     =39

class Camera(object):
    def __init__(self) :
        self.openCamera()

    def isCameraOpened(self) :
        return self.capture.isOpened()

    def openCamera(self) :
        self.capture = cv2.VideoCapture(Constant.CAMERA_ID)
        if not self.capture.isOpened():
            print("Camera not configured properly")
            return None

        # Loading default constants
        self.captureSize = Constant.RAW_CAPTURE_RES

        self.loadCameraStaParam()
        self.focus = self.capture.get(cv2.CAP_PROP_FOCUS)
        self.brightness = self.capture.get(cv2.CAP_PROP_BRIGHTNESS)
        self.contrast = self.capture.get(cv2.CAP_PROP_CONTRAST)
        self.hue = self.capture.get(cv2.CAP_PROP_HUE)
        self.gain = self.capture.get(cv2.CAP_PROP_GAIN)
        self.exposure = self.capture.get(cv2.CAP_PROP_EXPOSURE)

        # Disable autofocus
        #self.capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)

    def loadCameraDynParam(self):
        self.capture.set(cv2.CAP_PROP_SETTINGS, 1)

    def loadCameraStaParam(self):
        self.capture.set(3, self.captureSize[0])
        self.capture.set(4, self.captureSize[1])

    def captureOnce(self):
        returnVal, frame = self.capture.read()
        if returnVal == True :
            return frame
        else :
            return None

    def release(self):
        self.capture.release()
