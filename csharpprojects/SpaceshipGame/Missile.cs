using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;
using System.Windows.Forms;

namespace SpaceshipGame
{
    internal class Missile
    {
        private int _missileSpeed = 15;
        private PictureBox _missilePictureBox;
        private System.Windows.Forms.Timer _missileTimer = new System.Windows.Forms.Timer();
        private Image _imageSource = Properties.Resources.blast;

        private int _missileLeft;
        private int _missileTop;


        public Missile( int missileLeft, int missileTop, PictureBox missilePicBox)
        {
            _missileLeft= missileLeft;
            _missileTop= missileTop;
            _missilePictureBox = missilePicBox;
        }
        public int MissileLeft { get { return _missileLeft; } set { _missileLeft = value; } }
        public int MissileTop { get { return _missileTop; } set { _missileTop = value; } }
        public PictureBox MissilePictureBox { get { return _missilePictureBox; } set { _missilePictureBox = value; } }


        public void MakeMissile(Form form)
        {
            MissilePictureBox.BackColor = Color.Black;
            MissilePictureBox.Left = MissileLeft;
            MissilePictureBox.Top = MissileTop;
            MissilePictureBox.Image = _imageSource;
            //adding this picture box to the form
            form.Controls.Add(MissilePictureBox);
            MissilePictureBox.BringToFront();
            MissilePictureBox.Visible = true;
            //getting the missile timer to work: 
            _missileTimer.Interval = _missileSpeed;
            _missileTimer.Tick += new EventHandler(MissileTimer_Tick);
            _missileTimer.Start();
        }

        public void MissileTimer_Tick(object sender, EventArgs e)
        {
            MissilePictureBox.Top -= _missileSpeed;

            if (MissilePictureBox.Top <= 0)
            {
                //stop the missileTimer and get rid of it.
                _missileTimer.Stop();
                _missileTimer.Dispose();
                //move the missile off screen above the enemy ships:
                MissilePictureBox.Top = -300;
            }
        }

    }
}

//how to write to the console:
//System.Diagnostics.Debug.WriteLine("--this is working---");


