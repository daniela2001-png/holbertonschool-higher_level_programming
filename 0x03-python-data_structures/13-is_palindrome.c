#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - function that verficated a list
 * @head:main node
 * Return:1 is it is palindrome of list
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;/*puntero a nodos*/
	int largo = 0, start = 0;
	char buffer[100000];

	if (*head == NULL)
		return (1);
	temp = *head;
	while (temp != NULL)/* recorrermos lista*/
	{
		buffer[largo] = temp->n;
		largo++;
		temp = temp->next;
	}
	largo--;
	while (start < largo)/*verificamos si es palindroma*/
	{
		if (buffer[start] == buffer[largo])
		{
			start++;
			largo--;
		}
		else
			return (0);
	}
	return (1);
}