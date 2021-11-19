
namespace SPM_DAQ_WF_1
{
    partial class Frm_SPMDAQ
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea3 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            this.Lbl_Samples = new System.Windows.Forms.Label();
            this.Lbl_Period = new System.Windows.Forms.Label();
            this.NUD_Samples = new System.Windows.Forms.NumericUpDown();
            this.NUD_Period = new System.Windows.Forms.NumericUpDown();
            this.Btn_Start = new System.Windows.Forms.Button();
            this.Btn_Stop = new System.Windows.Forms.Button();
            this.Btn_Save = new System.Windows.Forms.Button();
            this.Ptl_SPM = new System.Windows.Forms.DataVisualization.Charting.Chart();
            ((System.ComponentModel.ISupportInitialize)(this.NUD_Samples)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.NUD_Period)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.Ptl_SPM)).BeginInit();
            this.SuspendLayout();
            // 
            // Lbl_Samples
            // 
            this.Lbl_Samples.AutoSize = true;
            this.Lbl_Samples.Location = new System.Drawing.Point(117, 57);
            this.Lbl_Samples.Name = "Lbl_Samples";
            this.Lbl_Samples.Size = new System.Drawing.Size(53, 13);
            this.Lbl_Samples.TabIndex = 0;
            this.Lbl_Samples.Text = "Samples: ";
            this.Lbl_Samples.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // Lbl_Period
            // 
            this.Lbl_Period.AutoSize = true;
            this.Lbl_Period.Location = new System.Drawing.Point(105, 128);
            this.Lbl_Period.Name = "Lbl_Period";
            this.Lbl_Period.Size = new System.Drawing.Size(62, 13);
            this.Lbl_Period.TabIndex = 1;
            this.Lbl_Period.Text = "Period (ms):";
            // 
            // NUD_Samples
            // 
            this.NUD_Samples.Location = new System.Drawing.Point(45, 73);
            this.NUD_Samples.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.NUD_Samples.Name = "NUD_Samples";
            this.NUD_Samples.Size = new System.Drawing.Size(120, 20);
            this.NUD_Samples.TabIndex = 3;
            this.NUD_Samples.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.NUD_Samples.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // NUD_Period
            // 
            this.NUD_Period.Location = new System.Drawing.Point(45, 144);
            this.NUD_Period.Maximum = new decimal(new int[] {
            2000,
            0,
            0,
            0});
            this.NUD_Period.Minimum = new decimal(new int[] {
            10,
            0,
            0,
            0});
            this.NUD_Period.Name = "NUD_Period";
            this.NUD_Period.Size = new System.Drawing.Size(120, 20);
            this.NUD_Period.TabIndex = 4;
            this.NUD_Period.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.NUD_Period.Value = new decimal(new int[] {
            10,
            0,
            0,
            0});
            // 
            // Btn_Start
            // 
            this.Btn_Start.Location = new System.Drawing.Point(57, 199);
            this.Btn_Start.Name = "Btn_Start";
            this.Btn_Start.Size = new System.Drawing.Size(98, 43);
            this.Btn_Start.TabIndex = 5;
            this.Btn_Start.Text = "Start";
            this.Btn_Start.UseVisualStyleBackColor = true;
            this.Btn_Start.Click += new System.EventHandler(this.Btn_Start_Click);
            // 
            // Btn_Stop
            // 
            this.Btn_Stop.Location = new System.Drawing.Point(57, 262);
            this.Btn_Stop.Name = "Btn_Stop";
            this.Btn_Stop.Size = new System.Drawing.Size(98, 43);
            this.Btn_Stop.TabIndex = 6;
            this.Btn_Stop.Text = "Stop";
            this.Btn_Stop.UseVisualStyleBackColor = true;
            this.Btn_Stop.Click += new System.EventHandler(this.Btn_Stop_Click);
            // 
            // Btn_Save
            // 
            this.Btn_Save.Location = new System.Drawing.Point(57, 329);
            this.Btn_Save.Name = "Btn_Save";
            this.Btn_Save.Size = new System.Drawing.Size(98, 43);
            this.Btn_Save.TabIndex = 7;
            this.Btn_Save.Text = "Save";
            this.Btn_Save.UseVisualStyleBackColor = true;
            this.Btn_Save.Click += new System.EventHandler(this.Btn_Save_Click);
            // 
            // Ptl_SPM
            // 
            chartArea3.Name = "ChartArea1";
            this.Ptl_SPM.ChartAreas.Add(chartArea3);
            this.Ptl_SPM.Location = new System.Drawing.Point(214, 39);
            this.Ptl_SPM.Name = "Ptl_SPM";
            this.Ptl_SPM.Size = new System.Drawing.Size(530, 378);
            this.Ptl_SPM.TabIndex = 8;
            this.Ptl_SPM.Text = "chart1";
            // 
            // Frm_SPMDAQ
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Ptl_SPM);
            this.Controls.Add(this.Btn_Save);
            this.Controls.Add(this.Btn_Stop);
            this.Controls.Add(this.Btn_Start);
            this.Controls.Add(this.NUD_Period);
            this.Controls.Add(this.NUD_Samples);
            this.Controls.Add(this.Lbl_Period);
            this.Controls.Add(this.Lbl_Samples);
            this.Name = "Frm_SPMDAQ";
            this.Text = "SPM DAQ & C#";
            this.Load += new System.EventHandler(this.Frm_SPMDAQ_Load);
            ((System.ComponentModel.ISupportInitialize)(this.NUD_Samples)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.NUD_Period)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.Ptl_SPM)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Lbl_Samples;
        private System.Windows.Forms.Label Lbl_Period;
        private System.Windows.Forms.NumericUpDown NUD_Samples;
        private System.Windows.Forms.NumericUpDown NUD_Period;
        private System.Windows.Forms.Button Btn_Start;
        private System.Windows.Forms.Button Btn_Stop;
        private System.Windows.Forms.Button Btn_Save;
        private System.Windows.Forms.DataVisualization.Charting.Chart Ptl_SPM;
    }
}

