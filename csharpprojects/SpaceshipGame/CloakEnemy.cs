using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpaceshipGame
{
    internal class CloakEnemy:Enemy
    {
        //private bool _hasPassed200;
        //private bool _hasPassed400;

        public CloakEnemy(int enemySpeed, int pointValue, Image enemyImage) : base(enemySpeed, pointValue, enemyImage)
        {

        }
        public override void MoveTheEnemy(PictureBox enemyBox)
        {
            //The enemy blinks in and out. 
            enemyBox.Top += EnemySpeed;
            if (enemyBox.Top > 200 && enemyBox.Top < 350)
            {
                enemyBox.Visible = false;
            }
            else if (enemyBox.Top >= 350)
            {
                enemyBox.Visible = true;
            }


            //if (!_hasPassed200)
            //{
            //    enemyBox.Top += EnemySpeed;
            //}

            //else if (enemyBox.Top > 200)
            //{
            //    _hasPassed200 = true;
            //    enemyBox.Visible = false;
            //    enemyBox.Left -= 50;
            //    enemyBox.Top = 200;

            //}
            //else if (_hasPassed200)
            //{
            //    enemyBox.Visible = true;
            //    enemyBox.Top += EnemySpeed;
            //}

            //else if (enemyBox.Top > 400 && _hasPassed200)
            //{
            //    _hasPassed400 = true;
            //    enemyBox.Visible = false;
            //    enemyBox.Left += 50;
            //    enemyBox.Top = 400;
            //}
            //else if (_hasPassed400 && _hasPassed200)
            //{
            //    enemyBox.Visible = true;
            //    enemyBox.Top += EnemySpeed;
            //}

        }
    }
}
