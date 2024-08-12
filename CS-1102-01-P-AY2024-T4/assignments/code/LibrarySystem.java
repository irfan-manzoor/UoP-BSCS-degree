import java.util.*;

class Book {
    String title;
    String author;
    int quantity;

    public Book(String title, String author, int quantity) {
        this.title = title;
        this.author = author;
        this.quantity = quantity;
    }
}

public class LibrarySystem {
    private static Map<String, Book> library = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nLibrary System Menu:");
            System.out.println("1. Add Books");
            System.out.println("2. Borrow Books");
            System.out.println("3. Return Books");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    addBooks(scanner);
                    break;
                case 2:
                    borrowBooks(scanner);
                    break;
                case 3:
                    returnBooks(scanner);
                    break;
                case 4:
                    System.out.println("Exiting program...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a number from 1 to 4.");
            }
        }
    }

    private static void addBooks(Scanner scanner) {
        System.out.print("Enter book title: ");
        String title = scanner.next();
        System.out.print("Enter author name: ");
        String author = scanner.next();
        System.out.print("Enter quantity: ");
        int quantity = scanner.nextInt();

        if (library.containsKey(title)) {
            Book existingBook = library.get(title);
            existingBook.quantity += quantity;
            System.out.println("Quantity updated for book: " + title);
        } else {
            library.put(title, new Book(title, author, quantity));
            System.out.println("Book added to library: " + title);
        }
    }

    private static void borrowBooks(Scanner scanner) {
        System.out.print("Enter book title: ");
        String title = scanner.next();
        System.out.print("Enter quantity to borrow: ");
        int quantity = scanner.nextInt();

        if (library.containsKey(title)) {
            Book book = library.get(title);
            if (book.quantity >= quantity) {
                book.quantity -= quantity;
                System.out.println("Successfully borrowed " + quantity + " copies of " + title);
            } else {
                System.out.println("Requested quantity not available for book: " + title);
            }
        } else {
            System.out.println("Book not found in library: " + title);
        }
    }

    private static void returnBooks(Scanner scanner) {
        System.out.print("Enter book title: ");
        String title = scanner.next();
        System.out.print("Enter quantity to return: ");
        int quantity = scanner.nextInt();

        if (library.containsKey(title)) {
            Book book = library.get(title);
            book.quantity += quantity;
            System.out.println("Successfully returned " + quantity + " copies of " + title);
        } else {
            System.out.println("Book not found in library: " + title);
        }
    }
}
