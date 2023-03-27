using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpaceshipGame
{
    internal class CloakEnemy:Enemy
    {

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

        }
    }
}
