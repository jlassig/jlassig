namespace SpaceshipGame
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

 
        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.spacePanel = new System.Windows.Forms.Panel();
            this.youWinLabel = new System.Windows.Forms.Label();
            this.missilePicBox2 = new System.Windows.Forms.PictureBox();
            this.missilePicBox3 = new System.Windows.Forms.PictureBox();
            this.missilePicBox = new System.Windows.Forms.PictureBox();
            this.enemyPicBox2 = new System.Windows.Forms.PictureBox();
            this.enemyPicBox1 = new System.Windows.Forms.PictureBox();
            this.playerPictureBox = new System.Windows.Forms.PictureBox();
            this.space2 = new System.Windows.Forms.PictureBox();
            this.space1 = new System.Windows.Forms.PictureBox();
            this.gameTimer = new System.Windows.Forms.Timer(this.components);
            this.btnStart = new System.Windows.Forms.Button();
            this.score = new System.Windows.Forms.Label();
            this.youWinTimer = new System.Windows.Forms.Timer(this.components);
            this.missileTimer = new System.Windows.Forms.Timer(this.components);
            this.spacePanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.missilePicBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.missilePicBox3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.missilePicBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.enemyPicBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.enemyPicBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.playerPictureBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.space2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.space1)).BeginInit();
            this.SuspendLayout();
            // 
            // spacePanel
            // 
            this.spacePanel.BackColor = System.Drawing.Color.Black;
            this.spacePanel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.spacePanel.Controls.Add(this.youWinLabel);
            this.spacePanel.Controls.Add(this.missilePicBox2);
            this.spacePanel.Controls.Add(this.missilePicBox3);
            this.spacePanel.Controls.Add(this.missilePicBox);
            this.spacePanel.Controls.Add(this.enemyPicBox2);
            this.spacePanel.Controls.Add(this.enemyPicBox1);
            this.spacePanel.Controls.Add(this.playerPictureBox);
            this.spacePanel.Controls.Add(this.space2);
            this.spacePanel.Controls.Add(this.space1);
            this.spacePanel.Location = new System.Drawing.Point(12, 12);
            this.spacePanel.Name = "spacePanel";
            this.spacePanel.Size = new System.Drawing.Size(476, 675);
            this.spacePanel.TabIndex = 0;
            // 
            // youWinLabel
            // 
            this.youWinLabel.AutoSize = true;
            this.youWinLabel.BackColor = System.Drawing.Color.Black;
            this.youWinLabel.Font = new System.Drawing.Font("Stencil", 48F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.youWinLabel.ForeColor = System.Drawing.Color.Red;
            this.youWinLabel.Location = new System.Drawing.Point(104, 226);
            this.youWinLabel.Name = "youWinLabel";
            this.youWinLabel.Size = new System.Drawing.Size(291, 76);
            this.youWinLabel.TabIndex = 14;
            this.youWinLabel.Text = "You Win";
            this.youWinLabel.Visible = false;
            // 
            // missilePicBox2
            // 
            this.missilePicBox2.Image = global::SpaceshipGame.Properties.Resources.blast;
            this.missilePicBox2.Location = new System.Drawing.Point(300,-200);
            this.missilePicBox2.Name = "missilePicBox2";
            this.missilePicBox2.Size = new System.Drawing.Size(10, 41);
            this.missilePicBox2.TabIndex = 13;
            this.missilePicBox2.TabStop = false;
            this.missilePicBox2.Visible = false;           
            // 
            // missilePicBox3
            // 
            this.missilePicBox3.Image = global::SpaceshipGame.Properties.Resources.blast;
            this.missilePicBox3.Location = new System.Drawing.Point(200,-200);
            this.missilePicBox3.Name = "missilePicBox3";
            this.missilePicBox3.Size = new System.Drawing.Size(10, 41);
            this.missilePicBox3.TabIndex = 12;
            this.missilePicBox3.TabStop = false;
            this.missilePicBox3.Visible = false;
            // 
            // missilePicBox
            // 
            this.missilePicBox.Image = global::SpaceshipGame.Properties.Resources.blast;
            this.missilePicBox.Location = new System.Drawing.Point(100,-200);
            this.missilePicBox.Name = "missilePicBox";
            this.missilePicBox.Size = new System.Drawing.Size(10, 41);
            this.missilePicBox.TabIndex = 11;
            this.missilePicBox.TabStop = false;
            this.missilePicBox.Visible = false;
            // 
            // enemyPicBox2
            // 
            this.enemyPicBox2.BackColor = System.Drawing.Color.Transparent;
            this.enemyPicBox2.Image = global::SpaceshipGame.Properties.Resources.greenEnemy;
            this.enemyPicBox2.Location = new System.Drawing.Point(38, -189);
            this.enemyPicBox2.Name = "enemyPicBox2";
            this.enemyPicBox2.Size = new System.Drawing.Size(100, 50);
            this.enemyPicBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.enemyPicBox2.TabIndex = 10;
            this.enemyPicBox2.TabStop = false;
            // 
            // enemyPicBox1
            // 
            this.enemyPicBox1.BackColor = System.Drawing.Color.Transparent;
            this.enemyPicBox1.Image = global::SpaceshipGame.Properties.Resources.redEnemy;
            this.enemyPicBox1.Location = new System.Drawing.Point(340, -150);
            this.enemyPicBox1.Name = "enemyPicBox1";
            this.enemyPicBox1.Size = new System.Drawing.Size(100, 50);
            this.enemyPicBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.enemyPicBox1.TabIndex = 9;
            this.enemyPicBox1.TabStop = false;
            // 
            // playerPictureBox
            // 
            this.playerPictureBox.BackColor = System.Drawing.Color.Transparent;
            this.playerPictureBox.Image = global::SpaceshipGame.Properties.Resources.player;
            this.playerPictureBox.Location = new System.Drawing.Point(167, 580);
            this.playerPictureBox.Name = "playerPictureBox";
            this.playerPictureBox.Size = new System.Drawing.Size(100, 50);
            this.playerPictureBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.playerPictureBox.TabIndex = 8;
            this.playerPictureBox.TabStop = false;
            // 
            // space2
            // 
            this.space2.Image = global::SpaceshipGame.Properties.Resources.spaceImage5;
            this.space2.Location = new System.Drawing.Point(0, 0);
            this.space2.Name = "space2";
            this.space2.Size = new System.Drawing.Size(476, 675);
            this.space2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.space2.TabIndex = 7;
            this.space2.TabStop = false;
            // 
            // space1
            // 
            this.space1.Image = global::SpaceshipGame.Properties.Resources.spaceImage1;
            this.space1.Location = new System.Drawing.Point(0, -675);
            this.space1.Name = "space1";
            this.space1.Size = new System.Drawing.Size(476, 675);
            this.space1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.space1.TabIndex = 1;
            this.space1.TabStop = false;
            // 
            // GameTimer
            // 
            this.gameTimer.Interval = 20;
            this.gameTimer.Tick += new System.EventHandler(this.GameTimerEvent);
            // 
            // btnStart
            // 
            this.btnStart.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.btnStart.Font = new System.Drawing.Font("Stencil", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.btnStart.Location = new System.Drawing.Point(181, 693);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(163, 44);
            this.btnStart.TabIndex = 8;
            this.btnStart.Text = "Play Game";
            this.btnStart.UseVisualStyleBackColor = false;
            this.btnStart.Click += new System.EventHandler(this.StartGame);
            // 
            // Score
            // 
            this.score.Font = new System.Drawing.Font("Stencil", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.score.Location = new System.Drawing.Point(181, 749);
            this.score.Name = "Score";
            this.score.Size = new System.Drawing.Size(163, 34);
            this.score.TabIndex = 10;
            this.score.Text = "Score: ";
            // 
            // YouWinTimer
            // 
            this.youWinTimer.Interval = 1000;
            this.youWinTimer.Tick += new System.EventHandler(this.YouWinTimerEvent);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.InactiveCaption;
            this.ClientSize = new System.Drawing.Size(507, 804);
            this.Controls.Add(this.score);
            this.Controls.Add(this.spacePanel);
            this.Controls.Add(this.btnStart);
            this.Name = "Form1";
            this.Text = "Spaceship Game";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.KeyIsDown);
            this.KeyUp += new System.Windows.Forms.KeyEventHandler(this.KeyIsUp);
            this.spacePanel.ResumeLayout(false);
            this.spacePanel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.missilePicBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.missilePicBox3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.missilePicBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.enemyPicBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.enemyPicBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.playerPictureBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.space2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.space1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.Timer gameTimer;
        private Button btnStart;
        private Panel spacePanel;
        private Label score;
        private System.Windows.Forms.Timer youWinTimer;
        private System.Windows.Forms.Timer missileTimer;
        private PictureBox space1;
        private PictureBox playerPictureBox;
        private PictureBox space2;
        private Label youWinLabel;
        private PictureBox missilePicBox2;
        private PictureBox missilePicBox3;
        private PictureBox missilePicBox;
        private PictureBox enemyPicBox2;
        private PictureBox enemyPicBox1;
    }
}