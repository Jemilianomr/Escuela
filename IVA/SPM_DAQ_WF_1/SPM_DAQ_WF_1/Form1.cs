using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
// Agregar refeerencias
using System.IO;
using NationalInstruments.DAQmx;
using NationalInstruments;
using System.Threading;

namespace SPM_DAQ_WF_1
{
    public partial class Frm_SPMDAQ : Form
    {
        int samples;
        int deltaTime;
        double[] time;
        double[] voltageCH0;

        NationalInstruments.DAQmx.Task analogInTask;
        AIChannel inputChannel0;
        AnalogSingleChannelReader aIReader;

        bool stopAcquisition = false;

        private bool DaqInit()
        {
            bool result = false;
            try{
                analogInTask = new NationalInstruments.DAQmx.Task();
                inputChannel0 = analogInTask.AIChannels.CreateVoltageChannel(
                    "DAQIVA/ai0","channel0", AITerminalConfiguration.Differential,
                    -10,10,AIVoltageUnits.Volts);
                aIReader = new AnalogSingleChannelReader(analogInTask.Stream);
                result = true;
            }
            catch
            {
                MessageBox.Show("The task wasn't created!");
                return false;
            }
            return result;
        } // DaqInit

        private int GetSamples()
        {
            int result;
            result = Convert.ToInt16(NUD_Samples.Value);
            return result;
        }

        private int GetPeriod()
        {
            int result;
            result = Convert.ToInt16(NUD_Period.Value);
            return result;
        }

        private async GetDelay()
        {

        }

        public Frm_SPMDAQ()
        {
            InitializeComponent();
        } // COnstructor

        private async void Btn_Start_Click(object sender, EventArgs e)
        {
            Btn_Save.Visible = false;
            Btn_Start.Visible = false;
            Btn_Stop.Visible = false;
            bool takeData = false;
            stopAcquisition = false;

            takeData = DaqInit();
            if (takeData == true)
            {
                samples = GetSamples();
                deltaTime = GetPeriod();
                Ptl_SPM.Series.Clear();
                Ptl_SPM.Series.Add("VoltageCh0");
                Ptl_SPM.Series["VoltageCh0"].ChartType =
                    System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
                Ptl_SPM.Series["VoltageCh0"].BorderWidth = 3;
                Ptl_SPM.Series["VoltageCh0"].BorderDashStyle = 
                    System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Dash;
                Ptl_SPM.Series["VoltageCh0"].MarkerStyle =
                    System.Windows.Forms.DataVisualization.Charting.MarkerStyle.Circle;
                Ptl_SPM.Series["VoltageCh0"].MarkerSize = 9;
                Ptl_SPM.Series["VoltageCh0"].Color = Color.OrangeRed;

                double t = 0;
                time = new double[0];
                voltageCH0 = new double[0];
                double tempVolt = 0;
                for(int i = 0; i < samples; i++)
                {
                    t = i * (deltaTime / 1000.0);

                    tempVolt = aIReader.ReadSingleExample();
                    Array.Resize(ref time, time.Length + 1);
                    time[time.Length - 1] = t;

                    tempVolt = aIReader.ReadSingleExample();
                    Array.Resize(ref voltageCH0, voltageCH0.Length + 1);
                    voltageCH0[voltageCH0.Length - 1] = tempVolt;

                    Ptl_SPM.Series["VoltageCh0"].Points.AddXY(t, tempVolt);

                    if(stopAcquisition == true)
                    {
                        break;
                    }

                    await GetDealy(deltaTime);

                }
            }
            else
            {
                MessageBox.Show("Data wasn't acquired");
            }

            Btn_Save.Visible = true;
            Btn_Start.Visible = true;
            Btn_Stop.Visible = false;

        }

        private void Frm_SPMDAQ_Load(object sender, EventArgs e)
        {
            Btn_Stop.Visible =false;
            Btn_Save.Visible =false;
        }
        private void Btn_Stop_Click(object sender, EventArgs e)
        {
            Btn_Start.Visible=false;
            Btn_Save.Visible=false;
            Btn_Stop.Visible=false;

            stopAcquisition = true;

            Thread.Sleep();

            Btn_Start.Visible = true;
            Btn_Save.Visible = true;
        }

        private string[] StringDataArray(int number)
        {
            int n = number;
            string[] values = new string[n + 1];

            values[0] = "Time_(s),Vch0_(V)";
            for (int i = 1; i < n+1; i++)
            {
                values[i] = Convert.ToString(time[i - 1]) + "," + Convert.ToString(voltageCH0[i - 1]);
            }
            return values;
        }

        private void Btn_Save_Click(object sender, EventArgs e)
        {
            Btn_Start.Visible = false;
            Btn_Stop.Visible = false;
            Btn_Save.Visible = false;

            Stream myStream;

            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.RestoreDirectory = true;
            if(saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                string[] values = StringDataArray(time.Length);
                if((myStream = saveFileDialog.OpenFile()) != null)
                {
                    using (StreamWriter writer = new StreamWriter(myStream))
                    {
                        for (int i = 0; i < values.Length; i++)
                        {
                            writer.WriteLine(values[i]);
                        }
                    }
                    myStream.Close();
                }
            }

            Btn_Start.Visible = true;
            Btn_Save.Visible = true;
        }
    } // Class
} // Namespace
 