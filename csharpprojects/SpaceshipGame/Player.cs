using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpaceshipGame
{
    internal class Player
    {

        private int _playerSpeed = 12;
        private int _score;

        public Player()
        {


        }

        public int Score { get { return _score; } set { _score = value; } }

        public void MovePlayer(PictureBox playerBox, bool goleft, bool goright)
        {
            //check to make sure the player hasn't left the bounds of the form. 
            if (goleft == true && playerBox.Left > 5)
            {
                playerBox.Left -= _playerSpeed;
            }
            if (goright == true && playerBox.Left < 370)
            {
                playerBox.Left += _playerSpeed;
            }

        }
         //this would probably need to be passed the Player's location and the Enemy's location.
        //public void CollisionDectectionPlayer() { }
    }

}
