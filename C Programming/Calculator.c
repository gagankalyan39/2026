#include <stdio.h>
int main() {
    int choice;
    float num1, num2, result;

    while (1) {
        printf("\nCALCULATOR \n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Multiplication\n");
        printf("4. Division\n");

        printf("Enter your choice (1-4): ");
        scanf("%d", &choice);

        // Check for invalid choice
        if (choice < 1 || choice > 4) {
            printf("Invalid choice! Please enter a number between 1 and 4.\n");
            continue;   // Show the menu again
        }

        printf("Enter first number: ");
        scanf("%f", &num1);

        printf("Enter second number: ");
        scanf("%f", &num2);

        switch (choice) {
            case 1:
                result = num1 + num2;
                printf("Result = %.2f\n", result);
                break;

            case 2:
                result = num1 - num2;
                printf("Result = %.2f\n", result);
                break;

            case 3:
                result = num1 * num2;
                printf("Result = %.2f\n", result);
                break;

            case 4:
                if (num2 == 0) {
                    printf("Error! Division by zero is not allowed.\n");
                } else {
                    result = num1 / num2;
                    printf("Result = %.2f\n", result);
                }
                break;
        }

        // Ask if the user wants another calculation
        int again;
        printf("\nDo you want to perform another calculation?\n");
        printf("1. Yes\n");
        printf("0. No\n");
        printf("Enter your choice: ");
        scanf("%d", &again);

        if (again == 0) {
            printf("Thank you for using the calculator!\n");
            break;
        }
    }

    return 0;

