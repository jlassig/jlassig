using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpaceshipGame
{
    internal class DiagonalEnemy:Enemy
    {
        private int _diagonalSpeed;

        public DiagonalEnemy(int enemySpeed, int pointValue, Image enemyImage, int diagonalSpeed) : base(enemySpeed, pointValue, enemyImage)
        {
            _diagonalSpeed = diagonalSpeed;
        }

        public int DiagonalSpeed { get { return _diagonalSpeed; } }

        public override void MoveTheEnemy(PictureBox enemyBox)
        {
            enemyBox.Top += EnemySpeed;
            enemyBox.Left -= DiagonalSpeed;
        }


    }


}
