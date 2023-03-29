using System.Reflection;
using System.Media;

namespace SpaceshipGame
{
    public partial class Form1 : Form
    {
        //speed for moving the background images
        private int _spaceSpeed;

        //this is how many seconds long the game goes until the "end of the game". 
        private int _timeLeft;

        private Player _player = new Player();
        

        //get some Randoms in there:
        private Random _spaceRand = new Random();
        private Random _rand = new Random();
        private Random _enemyPosition = new Random();
        //the ints that the randoms return when choosing an enemy. 
        private int _enemyImage;
        private int _enemyImage2;
        //the various bools, the first two are for the player
        private bool _goleft;
        private bool _goright;
        //and this one is so that we stop getting user input:
        private bool _isGameRunning;
        //well, if you get hit, then _isLoser = true! ha ha ha
        private bool _isLoser;

        //Oh yeah, added a 'pew' sound for my lasers! It makes them oh so scary for the enemies. lol
        SoundPlayer _pew = new SoundPlayer(@"C:\Users\Julia\Desktop\jlassig\csharpprojects\SpaceshipGame\Images\pew.wav");
        //a List to hold all the missiles.
        private List<Missile> _missiles= new List<Missile>();



        public Form1()
        {
            //pulls up the form
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // This was put in here by Visual Studio
        }

        //is the user pressing a key?
        private void KeyIsDown(object sender, KeyEventArgs e)
        {
            if (_isGameRunning)
            {
                //"e" == "event"
                //move the player Left and Right.
                //this gets sent to the Player Class. 

                if (e.KeyCode == Keys.Left)
                {
                    _goleft = true;

                }
                if (e.KeyCode == Keys.Right)
                {
                    _goright = true;
                }

            }

        }

            //did the user release the key? 
            private void KeyIsUp(object sender, KeyEventArgs e)
        {
            if (_isGameRunning)
            {
                //move the player the opposite of above. 
                if (e.KeyCode == Keys.Left)
                {
                    _goleft = false;

                }
                if (e.KeyCode == Keys.Right)
                {
                    _goright = false;
                }
                //fire a missile
                if (e.KeyCode == Keys.Space)
                {

                    FireMissile();
                    _pew.Play();

                }

            }

        }

        private void GameTimerEvent(object sender, EventArgs e)
        {
            //this is the label for the score:
            score.Text = ($"Score: {_player.Score}");

            //move the player:
            _player.MovePlayer(playerPictureBox, _goleft, _goright);


            //get a random number for the next enemy drawn, this makes it so the enemy isn't always the same.
            if (enemyPicBox1.Top <= -100)
            {
                _enemyImage = _rand.Next(1, 5);
            }
            if (enemyPicBox2.Top <= -100)
            {
                _enemyImage2 = _rand.Next(1, 4);
            }

            //now draw them
            DrawEnemy1(_enemyImage);
            DrawEnemy2(_enemyImage2);

            if (enemyPicBox1.Top > 675)
            {
                //set the EnemyTop somewhere randomly above the top of the screen between 
                //-99 and -130
                enemyPicBox1.Top = _enemyPosition.Next(99, 130) * -1;

                //If it's the right one:
                enemyPicBox1.Left = _enemyPosition.Next(230, 350);
            }

            if (enemyPicBox2.Top > 675)
            {
                enemyPicBox2.Top = _enemyPosition.Next(99, 130) * -1;

                //If it's the left one:
                enemyPicBox2.Left = _enemyPosition.Next(80, 230);
            }

            //there are two background PictureBoxes, space1 and space2.  
            //moving the background images:
            space1.Top += _spaceSpeed;
            space2.Top += _spaceSpeed;


            if (space1.Top > 675)
            {
                //this pulls a different image to use. space1 is the PictureBox for 
                ChangeSpaceImage(space1);
            }

            if (space2.Top > 675)
            {
                ChangeSpaceImage(space2);
            }

            //COLLISION DETECTION FOR THE PLAYER:
            if (playerPictureBox.Image != null && enemyPicBox1.Image != null && playerPictureBox.Bounds.IntersectsWith(enemyPicBox1.Bounds))
            {
                _isLoser = true;
                GameOver();
            }
            if (playerPictureBox.Image != null && enemyPicBox2.Image != null && playerPictureBox.Bounds.IntersectsWith(enemyPicBox2.Bounds))
            {
                _isLoser = true;
                GameOver();
            }
        }

        private void FireMissile()
        {
            //check to see if we need to remove any missing from the List of missiles
            CheckMissileStatus();

            if (_missiles.Count == 0)
            {
                Missile missile = new Missile((playerPictureBox.Left + (playerPictureBox.Width / 2)), (playerPictureBox.Top + (playerPictureBox.Height / 2)), missilePicBox);
                _missiles.Add(missile);
                missile.MakeMissile(this);
            }
            else if (_missiles.Count == 1)
            {

                Missile missile = new Missile((playerPictureBox.Left + (playerPictureBox.Width / 2)), (playerPictureBox.Top + (playerPictureBox.Height / 2)), missilePicBox2);
                _missiles.Add(missile);
                missile.MakeMissile(this);
            }
            else if (_missiles.Count == 2)
            {
                Missile missile = new Missile((playerPictureBox.Left + (playerPictureBox.Width / 2)), (playerPictureBox.Top + (playerPictureBox.Height / 2)), missilePicBox3);
                _missiles.Add(missile);
                missile.MakeMissile(this);
            }

        }

        //check to see if we need to remove any missiles from the List<Missile> _missiles
        private void CheckMissileStatus()
        {
            for (int i = _missiles.Count - 1; i >= 0; i--)
            {
                Missile missile = _missiles[i];
                if (missile.MissilePictureBox.Top <= 0)
                {
                    _missiles.RemoveAt(i);
                }
            }
        }

        //get a random space image:
        private void ChangeSpaceImage(PictureBox tempSpace)
        {
            //first get a random number: 
            int spaceImageNum = _spaceRand.Next(1, 6);
            if (spaceImageNum == 1)
            {
                //if it was the number 1, then draw the 1st image in the tempSpace pictureBox
                BackgroundImage s1 = new BackgroundImage(_spaceSpeed, Properties.Resources.spaceImage1);
                tempSpace.Image = s1.ImageSource;
            }
            else if (spaceImageNum == 2)
            {
                BackgroundImage s2 = new BackgroundImage(_spaceSpeed, Properties.Resources.spaceImage2);
                tempSpace.Image = s2.ImageSource;
            }
            else if (spaceImageNum == 3)
            {
                BackgroundImage s3 = new BackgroundImage(_spaceSpeed, Properties.Resources.spaceImage3);
                tempSpace.Image = s3.ImageSource;
            }
            else if (spaceImageNum == 4)
            {
                BackgroundImage s4 = new BackgroundImage(_spaceSpeed, Properties.Resources.spaceImage4);
                tempSpace.Image = s4.ImageSource;
            }
            else if (spaceImageNum == 5)
            {
                BackgroundImage s5 = new BackgroundImage(_spaceSpeed, Properties.Resources.spaceImage5);
                tempSpace.Image = s5.ImageSource;
            }

            //set the tempSpace pictureBox, that now has a new image, above the screen.
            tempSpace.Top = -675;

        }

        //draw the enemy in enemyPicBox1 (the right enemy)
        private void DrawEnemy1(int enemyImage)
        {
            int points = 0;

            if (enemyImage == 1)
            {

                //creating a new Enemy
                VerticalEnemy v = new VerticalEnemy(15, 30, Properties.Resources.greenEnemy);
                //getting the image for the green ship
                enemyPicBox1.Image = v.EnemyImage;
                if (enemyPicBox1.Top < 675)
                {
                    //move the enemy!!!
                    v.MoveTheEnemy(enemyPicBox1);
                }
                points = v.PointValue;
            }
            else if (enemyImage == 2)
            {
                HorizontalEnemy h = new HorizontalEnemy(8, 10, Properties.Resources.redEnemy, 2);

                enemyPicBox1.Image = h.EnemyImage;
                if (enemyPicBox1.Top < 675)
                {
                    h.MoveTheEnemy(enemyPicBox1);
                }
                points = h.PointValue;

            }
            else if (enemyImage == 3)
            {
                CloakEnemy c = new CloakEnemy(9, 20, Properties.Resources.purpleEnemy);
                enemyPicBox1.Image = c.EnemyImage;
                if (enemyPicBox1.Top < 675)
                {
                    c.MoveTheEnemy(enemyPicBox1);
                }
                points= c.PointValue;

            }
            else if (enemyImage == 4)
            {
                DiagonalEnemy d = new DiagonalEnemy(9, 20, Properties.Resources.leftAsteroid, 3);

                enemyPicBox1.Image = d.EnemyImage;
                if (enemyPicBox1.Top < 675)
                {
                    d.MoveTheEnemy(enemyPicBox1);
                }
                points= d.PointValue;

            }
            MissileCollisionDetection(missilePicBox, enemyPicBox1, points);
            MissileCollisionDetection(missilePicBox2, enemyPicBox1, points);
            MissileCollisionDetection(missilePicBox3, enemyPicBox1, points);

        }
        //and same thing for enemyPicBox2
        private void DrawEnemy2(int enemyImage)
        {
            int points = 0;

            if (enemyImage == 1)
            {

                //creating a new Enemy
                VerticalEnemy v = new VerticalEnemy(15, 30, Properties.Resources.greenEnemy);
                //getting the image for the green ship
                enemyPicBox2.Image = v.EnemyImage;
                if (enemyPicBox2.Top < 675)
                {
                    //moving the enemy:
                    v.MoveTheEnemy(enemyPicBox2);
                }
                points = v.PointValue;

            }
            else if (enemyImage == 2)
            {
                HorizontalEnemy h = new HorizontalEnemy(8, 10, Properties.Resources.redEnemy, 2);

                enemyPicBox2.Image = h.EnemyImage;
                if (enemyPicBox2.Top < 675)
                {
                    h.MoveTheEnemy(enemyPicBox2);
                }
                points= h.PointValue;

            }
            else if (enemyImage == 3)
            {
                CloakEnemy c = new CloakEnemy(9, 20, Properties.Resources.purpleEnemy);
                enemyPicBox2.Image = c.EnemyImage;
                if (enemyPicBox2.Top < 675)
                {
                    c.MoveTheEnemy(enemyPicBox2);
                }
                points= c.PointValue;

            }
            MissileCollisionDetection(missilePicBox, enemyPicBox2, points);
            MissileCollisionDetection(missilePicBox2, enemyPicBox2, points);
            MissileCollisionDetection(missilePicBox3, enemyPicBox2, points);
        }

        private void MissileCollisionDetection(PictureBox missileBox, PictureBox enemyBox, int points)
        {
            if(missileBox.Bounds.IntersectsWith(enemyBox.Bounds))
            {                
                missileBox.Top = -300;
                enemyBox.Top = _enemyPosition.Next(99, 130) * -1;
                enemyBox.Left = _enemyPosition.Next(230, 350);
                _player.Score += points;                
            }
        }

        private void YouWinTimerEvent(Object sender, EventArgs e)
        {
            if (_isLoser)
            {
                _timeLeft = 0;

            }
            else if (_timeLeft > 0)
            {
                _timeLeft--;
                youWinLabel.Visible = false;
                btnStart.Enabled = false;

            }
            else if (_timeLeft <= 0)
            {
                _isGameRunning = false;
                youWinLabel.Visible = true;
                btnStart.Enabled = true;
                _spaceSpeed = 0;
                gameTimer.Stop();

            }
        }


        private void GameOver()
        {
            _isGameRunning = false;
            gameTimer.Stop();
            _spaceSpeed = 0;
            btnStart.Enabled = true;
            youWinLabel.Text = "You Lose";
            youWinLabel.Visible = true;

        }

        //when the user clicks the button to Play the Game
        private void StartGame(object sender, EventArgs e)
        {
            _isGameRunning = false;
            //starts the game when the button is clicked
            ResetGame();
        }

        //after the user dies or wins, they can restart the game by clicking the button 
        //and all the variables get reset
        private void ResetGame()
          {
            _player.Score = 0;
            missilePicBox.Top = -300;
            missilePicBox2.Top = -300;
            missilePicBox3.Top = -300;
            enemyPicBox2.Top = -189;
            enemyPicBox1.Top = -150;
            _isGameRunning = true;
            _goleft = false;
            _goright = false;
            btnStart.Enabled = false;
            youWinTimer.Enabled = true;
            youWinLabel.Text = "You Win";
            youWinLabel.Visible = false;
            _timeLeft = 20;
            _spaceSpeed = 8;
            _isLoser= false;

            gameTimer.Start();

        }
    }
}