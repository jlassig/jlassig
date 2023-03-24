using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpaceshipGame
{
    internal class BackgroundImage
    {
        private int _imageSpeed;
        private Image _imageSource;
        //private bool _isEndImage;
        //private List<Image> _images;

        public BackgroundImage(int imageSpeed, Image imageSource)
        {
            _imageSpeed = imageSpeed;
            _imageSource = imageSource;
        }

        public Image ImageSource { get { return _imageSource; } }
        public int ImageSpeed { get { return _imageSpeed; } }

        //public void DrawBackground1(screen to draw on from Form1)
        //{

        //}

        //public int GetNextBGImage() { }


    }
}




