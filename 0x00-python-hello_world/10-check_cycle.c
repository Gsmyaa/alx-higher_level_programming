#include "lists.h"

/**
 * check_cycle - checks if a cycle exists
 * @list: linked list to be check
 *
 * Return: 1 if a cycle exists, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *sound = list;
	listint_t *light= list;

	if (!list)
		return (0);

	while (sound && light && light->next)
	{
		sound = sound->next;
		light = light->next->next;
		if (sound == light)
		{
			return (1);
		}
	}

	return (0);
}
