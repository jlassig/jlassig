using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpaceshipGame
{
    internal class VerticalEnemy:Enemy
    {

        public VerticalEnemy(int enemySpeed, int pointValue, Image enemyImage) : base(enemySpeed, pointValue, enemyImage)
        {

        }

        public override void MoveTheEnemy(PictureBox enemyBox)
        {
            enemyBox.Top += EnemySpeed;
        }
    }
}
