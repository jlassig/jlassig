using System.Reflection;
using System.Media;

namespace SpaceshipGame
{
    public partial class Form1 : Form
    {
        //speed for moving the background images
        private int _spaceSpeed;

        //this is how many seconds long the game goes until the "end of the game". 
        private int _timeLeft = 5;

        private Player _player = new Player();

        //get some Randoms in there:
        private Random _spaceRand = new Random();
        private Random _rand = new Random();
        private Random _enemyPosition = new Random();
        //the ints that the randoms return when choosing an enemy. 
        private int _enemyImage;
        private int _enemyImage2;

        bool _goleft;
        bool _goright;
        bool _isGameRunning;
        bool _isMissileFired;
        bool _isLoser;

        SoundPlayer _pew = new SoundPlayer(@"C:\Users\Julia\Desktop\jlassig\csharpprojects\SpaceshipGame\Images\pew.wav");



        public Form1()
        {
            //pulls up the form
            InitializeComponent();

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //I don't know what this does. This was put in here by Visual Studio
        }

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

                //fire a missile
                if (e.KeyCode == Keys.Space)
                {
                    _isMissileFired = true;
                    //setting the missilePicBox to the location of the Player
                    missilePicBox.Location = new Point((playerPictureBox.Location.X + 50), (playerPictureBox.Location.Y - 38));
                    _pew.Play();
                }
            }

        }

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
            }

        }

        private void GameTimerEvent(object sender, EventArgs e)
        {

            bool missileReady1 = _player.IsMissileReady("missile1");

            _player.MovePlayer(playerPictureBox, _goleft, _goright);

            if (enemyPicBox1.Top <= -100)
            {
                _enemyImage = _rand.Next(1, 5);
            }
            if (enemyPicBox2.Top <= -100)
            {
                _enemyImage2 = _rand.Next(1, 4);
            }

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

            //there are two PictureBoxes, space1 and space2.  
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

            if (_isMissileFired)
            {
                //isMissileFired= false;
                //if (!isMissileFired && missileReady1)
                //{
                _player.FireMissile("missile1");
            }
            //isMissileFired = false;


            //COLLISION DETECTION FOR THE PLAYER:
            if (playerPictureBox.Bounds.IntersectsWith(enemyPicBox1.Bounds) || playerPictureBox.Bounds.IntersectsWith(enemyPicBox2.Bounds))
            {
                _isLoser = true;
                //GameOver(); // when an enemy hits the player
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
                //COLLISION DETECTION FOR THE MISSILE: 
                if (missilePicBox.Bounds.IntersectsWith(enemyPicBox1.Bounds))
                {                    //set the EnemyTop somewhere randomly above the top of the screen between 
                    //-99 and -130

                    enemyPicBox1.Top = _enemyPosition.Next(99, 130) * -1;

                    //If it's the right one:
                    enemyPicBox1.Left = _enemyPosition.Next(230, 350);
                    _player.Score += v.PointValue;

                }
            }
            else if (enemyImage == 2)
            {
                HorizontalEnemy h = new HorizontalEnemy(8, 10, Properties.Resources.redEnemy, 2);

                enemyPicBox1.Image = h.EnemyImage;
                if (enemyPicBox1.Top < 675)
                {
                    h.MoveTheEnemy(enemyPicBox1);
                }

                if (missilePicBox.Bounds.IntersectsWith(enemyPicBox1.Bounds))
                {

                    //set the EnemyTop somewhere randomly above the top of the screen between 
                    //-99 and -130
                    enemyPicBox1.Top = _enemyPosition.Next(99, 130) * -1;

                    //If it's the right one:
                    enemyPicBox1.Left = _enemyPosition.Next(230, 350);

                    _player.Score += h.PointValue;
                }


            }
            else if (enemyImage == 3)
            {
                CloakEnemy c = new CloakEnemy(9, 20, Properties.Resources.purpleEnemy);
                enemyPicBox1.Image = c.EnemyImage;
                if (enemyPicBox1.Top < 675)
                {
                    c.MoveTheEnemy(enemyPicBox1);
                }
                if (missilePicBox.Bounds.IntersectsWith(enemyPicBox1.Bounds))
                {

                    //set the EnemyTop somewhere randomly above the top of the screen between 
                    //-99 and -130
                    enemyPicBox1.Top = _enemyPosition.Next(99, 130) * -1;

                    //If it's the right one:
                    enemyPicBox1.Left = _enemyPosition.Next(230, 350);

                    _player.Score += c.PointValue;
                }

            }
            else if (enemyImage == 4)
            {
                DiagonalEnemy d = new DiagonalEnemy(9, 20, Properties.Resources.leftAsteroid, 3);

                enemyPicBox1.Image = d.EnemyImage;
                if (enemyPicBox1.Top < 675)
                {
                    d.MoveTheEnemy(enemyPicBox1);
                }
                if (missilePicBox.Bounds.IntersectsWith(enemyPicBox1.Bounds))
                {

                    //set the EnemyTop somewhere randomly above the top of the screen between 
                    //-99 and -130
                    enemyPicBox1.Top = _enemyPosition.Next(99, 130) * -1;

                    //If it's the right one:
                    enemyPicBox1.Left = _enemyPosition.Next(230, 350);

                    _player.Score += d.PointValue;
                }


            }
        }
        //and same thing for enemyPicBox2
        private void DrawEnemy2(int enemyImage)
        {

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
                //COLLISION DETECTION FOR THE MISSILE: 
                if (missilePicBox.Bounds.IntersectsWith(enemyPicBox2.Bounds))
                {  //set the EnemyTop somewhere randomly above the top of the screen between 
                    //-99 and -130

                    enemyPicBox2.Top = _enemyPosition.Next(99, 130) * -1;

                    //If it's the right one:
                    enemyPicBox2.Left = _enemyPosition.Next(230, 350);
                    _player.Score += v.PointValue;

                }
            }
            else if (enemyImage == 2)
            {
                HorizontalEnemy h = new HorizontalEnemy(8, 10, Properties.Resources.redEnemy, 2);

                enemyPicBox2.Image = h.EnemyImage;
                if (enemyPicBox2.Top < 675)
                {
                    h.MoveTheEnemy(enemyPicBox2);
                }
                //COLLISION DETECTION FOR THE MISSILE: 
                if (missilePicBox.Bounds.IntersectsWith(enemyPicBox2.Bounds))
                {
                    enemyPicBox2.Top = _enemyPosition.Next(99, 130) * -1;
                    enemyPicBox2.Left = _enemyPosition.Next(230, 350);
                    _player.Score += h.PointValue;

                }


            }
            else if (enemyImage == 3)
            {
                CloakEnemy c = new CloakEnemy(9, 20, Properties.Resources.purpleEnemy);
                enemyPicBox2.Image = c.EnemyImage;
                if (enemyPicBox2.Top < 675)
                {
                    c.MoveTheEnemy(enemyPicBox2);
                }
                //COLLISION DETECTION FOR THE MISSILE: 
                if (missilePicBox.Bounds.IntersectsWith(enemyPicBox2.Bounds))
                {
                    enemyPicBox2.Top = _enemyPosition.Next(99, 130) * -1;
                    enemyPicBox2.Left = _enemyPosition.Next(230, 350);
                    _player.Score += c.PointValue;

                }

            }
        }



        private void YouWinTimerEvent(Object sender, EventArgs e)
        {
            if (_isLoser)
            {
                _timeLeft = 0;
                GameOver();
            }


            else if (_timeLeft > 0)
            {
                _timeLeft--;
                youWinLabel.Visible = false;
                btnStart.Enabled = false;
                Score.Text = ($"Score: {_player.Score}");
            }
            else if (_timeLeft <= 0)
            {

                _isGameRunning = false;
                youWinLabel.Visible = true;
                btnStart.Enabled = true;

                _spaceSpeed = 0;
                GameTimer.Stop();

                //maybe run GameOver() here?  instead and put the above values in 
                //GameOver. Also have a boolean value if you win or lose. 
                //GameOver needs a Lose screen, too
                //If you win, There could also be a FUNCTION that checks
                //to see how your score matches up and if you're the high score
                //you get to put in your initials like ol' school games
                //in a txt file. 

            }


        }


        private void GameOver()
        {
            _isGameRunning = false;
            GameTimer.Stop();
            _spaceSpeed = 0;
            btnStart.Enabled = true;
            enemyPicBox2.Top = -189;
            enemyPicBox1.Top = -150;
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
        private void ResetGame()
        {

            _player.EmptyDictionary();
            _player.FillInDictionary(missilePicBox, missilePicBox2, missilePicBox3);
            _isGameRunning = true;
            _goleft = false;
            _goright = false;
            btnStart.Enabled = false;
            YouWinTimer.Enabled = true;
            youWinLabel.Text = "You Win";
            youWinLabel.Visible = false;
            _timeLeft = 5;
            _spaceSpeed = 8;
            _player.Score = 0;
            _isLoser= false;



            GameTimer.Start();

        }
    }
}