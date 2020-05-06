#include "lists.h"
/**
 * recpal - Check if the linked list is palindrome
 * @left: Head of list
 * @right: Last element of recursion
 * Return: If is palindrome or not
 */
int result(listint_t **left, listint_t *right)
{
	int var1;

	if (right == NULL)
		return (1);

	var1 = result(left, right->next);
	if (var1 == 0)
		return (0);

	var1 = (right->n == (*left)->n);

	*left = (*left)->next;
	return (var1);
}
/**
 * is_palindrome - Check if the linked list is palindrome
 * @head: Take a list
 * Return: If is palindrome or not
 */
int is_palindrome(listint_t **head)
{
	int var1;

	if (!head)
		return (0);
	var1 = result(head, *head);
	return (var1);
}
