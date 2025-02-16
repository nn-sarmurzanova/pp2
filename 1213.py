using System;
using System.Drawing;
using System.Windows.Forms;

namespace BirthdayGreeting
{
    public class GreetingForm : Form
    {
        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);

            Graphics g = e.Graphics;
            
            // Создание фона
            g.Clear(Color.White);

            // Добавление поздравительного текста
            string greetingText = "С Днем Рождения, Наиля!";
            Font font = new Font("Arial", 24);
            Brush brush = Brushes.Black;
            PointF point = new PointF(50, 50);
            g.DrawString(greetingText, font, brush, point);

            // Загрузка изображения (замените путь на ваш собственный)
            string imagePath = "path/to/ryan_gosling_image_with_flowers.jpg";
            Image image = Image.FromFile(imagePath);

            // Отрисовка изображения
            Point imageLocation = new Point(50, 100);
            g.DrawImage(image, imageLocation);
        }

        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new GreetingForm());
        }
    }
}
