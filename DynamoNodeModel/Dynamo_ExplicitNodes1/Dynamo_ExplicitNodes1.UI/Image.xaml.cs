using AForge.Video;
using AForge.Video.DirectShow;
using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Threading;
using System.Windows;
using System.Windows.Media.Imaging;
using Dynamo_ExplicitNodes1.UI;

namespace Dynamo_ExplicitNodes1.UI
{
    public partial class Image : System.Windows.Controls.UserControl
    {
        public static FilterInfoCollection LocalWebCamsCollection; 
        public static VideoCaptureDevice LocalWebCam; 
        public BitmapImage currentFrame;

        public Image()
        {
            InitializeComponent();
            LocalWebCamsCollection = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            LocalWebCam = new VideoCaptureDevice(LocalWebCamsCollection[0].MonikerString);
            Loaded += MainWindow_Loaded;
        }

        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                System.Drawing.Image img = (Bitmap)eventArgs.Frame.Clone();

                MemoryStream ms = new MemoryStream();
                img.Save(ms, ImageFormat.Bmp);
                ms.Seek(0, SeekOrigin.Begin);
                BitmapImage bi = new BitmapImage();
                bi.BeginInit();
                bi.StreamSource = ms;
                currentFrame = bi;
                bi.EndInit();

                bi.Freeze();
                Dispatcher.BeginInvoke(new ThreadStart(delegate
                {
                    frameHolder.Source = bi;
                }));
            }
            catch (Exception ex) { MessageBox.Show(ex.Message); }
        }
        void MainWindow_Loaded(object sender, RoutedEventArgs e)
        {
            LocalWebCam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
            LocalWebCam.Start();
        }

        private void ImageCaptureButton_Click(object sender, RoutedEventArgs e)
        {
            BitmapImage frame = currentFrame;
            string directoryPath = $@"C:\Users\{Environment.UserName}\AppData\Local\FaceMesh\Images\";

            BitmapEncoder encoder = new PngBitmapEncoder();
            encoder.Frames.Add(BitmapFrame.Create(currentFrame));

            using (MemoryStream outStream = new MemoryStream())
            {
                BitmapEncoder enc = new BmpBitmapEncoder();
                enc.Frames.Add(BitmapFrame.Create(currentFrame));
                enc.Save(outStream);
                Bitmap bitmap = new Bitmap(outStream);
                var filepath = $@"{directoryPath}\{WebcamCapture.SelfieFilename}.jpg";
                File.Delete(filepath);

                using (var fileStream = new FileStream(filepath, FileMode.Create))
                {
                    EncoderParameters encoderParameters = new EncoderParameters(1);
                    ImageCodecInfo[] myCodecs = ImageCodecInfo.GetImageEncoders();
                    ImageCodecInfo jpegCodec = myCodecs[1];
                    encoderParameters.Param[0] = new EncoderParameter(Encoder.Quality, 100L);
                    bitmap.Save(fileStream, jpegCodec, encoderParameters);
                }
            }
        }
    }
}
