//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace SpaceshipGame
//{
//    internal class Missile
//    {
//        private int _missileSpeed = -5;
//        private string _missileState1 = "ready";
//        //private string _missileState2 = "ready";
//        //private string _missileState3 = "ready";








//        public void FireMissile(int x, int y, PictureBox missilePictureBox)
//        {
//            if (_missileState1 == "ready")
//            {
//                _missileState1 = "fire";
//                missilePictureBox.Location = new Point(x, y);
//                missilePictureBox.Visible = true;
//                while(missilePictureBox.Visible) 
//                {
//                    missilePictureBox.Top += _missileSpeed;
//                    if (missilePictureBox.Top <= 0)
//                    {
//                        _missileState1 = "ready";
//                        missilePictureBox.Visible = false;
//                    }

//                }

//            }


            
//        }

//    }



//}
