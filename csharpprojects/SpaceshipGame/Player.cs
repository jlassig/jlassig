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
        //private int _score;
        private int _playerSpeed = 12;
        //missile Dictionary has the Picture Box (there are 3), plus the "state": ready or fire
        private Dictionary<string, Tuple<PictureBox, string>> missileDictionary = new Dictionary<string, Tuple<PictureBox, string>>();
        private int _missileSpeed = 10;
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
        public void EmptyDictionary()
        {
            missileDictionary.Clear();
        }
        public void FillInDictionary(PictureBox m1, PictureBox m2, PictureBox m3)
        {//creating a dictionary of the missiles
            missileDictionary.Add("missile1",Tuple.Create(m1, "ready"));
            missileDictionary.Add("missile2", Tuple.Create(m2, "ready"));
            missileDictionary.Add("missile3", Tuple.Create(m3, "ready"));
        }

        //public void PrintDictionary()
        //{
        //    foreach (Tuple<PictureBox, string> value in missileDictionary.Values)
        //    {
        //        PictureBox pictureBox = value.Item1;
                
        //        System.Diagnostics.Debug.WriteLine(pictureBox.Name); 
        //    }
        //}
        public bool IsMissileReady(string missileName)
        {
            Tuple<PictureBox, string> missileValues = missileDictionary[missileName];
            string missileState = missileValues.Item2;
            if (missileState == "ready")
            {
                return true;
            }
            else
            {
                return false;
            }

        }


            //public void FireMissile1(int x, int y)
            public void FireMissile(string missileName)
            {
                //first get the values from the dictionary
                Tuple<PictureBox, string> missileValues = missileDictionary[missileName];
                //get the missilePictureBox
                PictureBox missileBox = missileValues.Item1;
            //System.Diagnostics.Debug.WriteLine(missileBox.Name);

            //changing the state to "fired"
            Tuple<PictureBox, string> updateMissileState = Tuple.Create(missileValues.Item1, "fired");
            //putting that back in the dictionary
                missileDictionary[missileName] = updateMissileState;

                //making the missile visible
                missileBox.Visible = true;
                //making the missile move
                missileBox.Top -= _missileSpeed;
                //if the missile has left the form:
                if (missileBox.Top < 0)
                {   
                    //update the missileState to now be ready because that missile is no longer on screen
                    updateMissileState = Tuple.Create(missileValues.Item1, "ready");
                //update the dictionary again
                    missileDictionary[missileName] = updateMissileState;
                //make the missile invisibile.
                    //missileBox.Visible = false;
                }

          }

        //this would probably need to be passed the Player's location and the Enemy's location.
        //public void CollisionDectectionPlayer() { }



        }

}
