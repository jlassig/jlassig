using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpaceshipGame
{
    internal class HorizontalEnemy:Enemy
    {
        private int _horizontalSpeed;
        private bool _isMovingRight = true;


        public HorizontalEnemy(int enemySpeed, int pointValue, Image enemyImage, int horizontalSpeed) : base(enemySpeed, pointValue, enemyImage)
        {
            _horizontalSpeed= horizontalSpeed;

        }

        public int HorizontalSpeed { get { return _horizontalSpeed; } }


        public override void MoveTheEnemy(PictureBox enemyBox)
        {

                enemyBox.Top += EnemySpeed;


                if (_isMovingRight)
                {
                    enemyBox.Left += HorizontalSpeed;
                    if (enemyBox.Left > 304)
                    {
                        _isMovingRight = false;

                    }
                }
 
                if (_isMovingRight == false)
                {
                    enemyBox.Left -= 200;
                    if (enemyBox.Left < 100)
                    {
                        _isMovingRight = true;
                    }


                }
            

        }
    }
}
