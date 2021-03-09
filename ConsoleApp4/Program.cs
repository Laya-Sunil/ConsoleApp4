using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace ConsoleApp4
{
    class Program
    {
        public static List<String> Names = new List<string> { "Zac", "Mara", "Scarlet", "Lilly", "Luke" };
        static void Main(string[] args)
        {
            DisplayCount();
            int c =DisplayNames();
            TotalCount(c);
            Console.ReadKey();
        }
        public static async Task DisplayCount()
        {
           
            await Task.Run(() =>
            {
                foreach (var name in Names)
                {

                    Console.WriteLine(name);
                    
                    Task.Delay(150).Wait();
                }

            });
            //TotalCount(count);
        }


        public static int DisplayNames()
        {
            int count = 0;
            foreach (var item in Names)
            {
                count += 1;
                //Console.WriteLine("Count = " + count);
                Console.WriteLine("Counting");
                
                Task.Delay(150).Wait();
            }
            return count;
        }
        public static void TotalCount(int c)
        {
            Console.WriteLine("total count = " + c);
        }
    }
}

