using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace SpaceshipGame
{
    internal abstract class Enemy
    {
        private int _enemySpeed;
        private int _pointValue;
        private Image _enemyImage;  //System.Drawing.Image is a "type" like a string or bool or int
        

        public Enemy(int enemySpeed, int pointValue, Image enemyImage)
        {
            _enemySpeed = enemySpeed;
            _pointValue = pointValue;
            _enemyImage = enemyImage;

        }

        public int PointValue { get { return _pointValue; } }

        public int EnemySpeed { get { return _enemySpeed; } }

        public Image EnemyImage { get { return _enemyImage; } }

        public abstract void MoveTheEnemy(PictureBox enemyBox);

        //pass this one the missilePictureBox location and the enemyPictureBox location?
        //public void CollisionDetectionEnemy() { }


    }
}
