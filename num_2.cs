// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;

namespace num2
{
    // Base class: Book
    class Book
    {
        private string title;
        private string author;
        private string isbn;

        public string Title
        {
            get { return title; }
            set { title = value; }
        }

        public string Author
        {
            get { return author; }
            set { author = value; }
        }

        public string ISBN
        {
            get { return isbn; }
            set { isbn = value; }
        }

        public Book(string title, string author, string isbn)
        {
            this.title = title;
            this.author = author;
            this.isbn = isbn;
        }

        public virtual Dictionary<string, string> GetDetails()
        {
            return new Dictionary<string, string>
            {
                {"title", Title},
                {"author", Author},
                {"isbn", ISBN}
            };
        }
    }

    // Derived class: PrintedBook
    class PrintedBook : Book
    {
        private int pages;

        public int Pages
        {
            get { return pages; }
            set { pages = value; }
        }

        public PrintedBook(string title, string author, string isbn, int pages)
            : base(title, author, isbn)
        {
            this.pages = pages;
        }

        public override Dictionary<string, string> GetDetails()
        {
            var details = base.GetDetails();
            details.Add("pages", pages.ToString());
            return details;
        }
    }

    // Derived class: EBook
    class EBook : Book
    {
        private int mbSize;
        private string format;

        public int MbSize
        {
            get { return mbSize; }
            set { mbSize = value; }
        }

        public string Format
        {
            get { return format; }
            set { format = value; }
        }

        public EBook(string title, string author, string isbn, int mbSize, string format)
            : base(title, author, isbn)
        {
            this.mbSize = mbSize;
            this.format = format;
        }

        public override Dictionary<string, string> GetDetails()
        {
            var details = base.GetDetails();
            details.Add("mb_size", mbSize.ToString());
            details.Add("format", format);
            return details;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Book> books = new List<Book>
            {
                new Book("Harry Potter", "JK Rowling", "123-456-789"),
                new PrintedBook("Cujo", "Stephen Hawking", "456-789-123", 600),
                new EBook("1984", "George Orwell", "789-456-123", 25, "pdf")
            };

            foreach (var book in books)
            {
                Console.WriteLine($"{book.GetType().Name}:");
                foreach (var detail in book.GetDetails())
                {
                    Console.WriteLine($"\t{detail.Key}: {detail.Value}");
                }
                Console.WriteLine();
            }
        }
    }
}