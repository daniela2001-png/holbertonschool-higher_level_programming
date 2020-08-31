#include "lists.h"

/**
 * check_cycle - validate if a SLK had a loop
 * @list: is the single linked list
 * Return: 0 if not found a loop else return 1
 */


int check_cycle(listint_t *list)
{

	listint_t *slow = NULL;
	listint_t *quick = NULL;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	quick = list->next->next;

	while (quick != NULL && slow != NULL && quick->next != NULL)
	{
		if (quick == slow)
			return (1);
		slow = slow->next;
		quick = quick->next->next;
	}
	return (0);
}
