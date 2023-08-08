#include "lists.h"

/**
  * check_cycle - Check if a singly linked list has a cycle.
  * @head: pointer to the head of the linked list.
  *
  * Return: 1 if a cycle is detected, 0 if no cycle is found.
  */
int check_cycle(listint_t *head)
{
	listint_t *slowPointer = head;
	listint_t *fastPointer = head;

	if (head == NULL || head->next == NULL)
		return (0);

	while (fastPointer != NULL && fastPointer->next != NULL)
	{
		slowPointer = slowPointer->next;
		fastPointer = fastPointer->next->next;

		if (slowPointer == fastPointer)
			return (1);
	}

	return (0);
}
