#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - infinite while loop
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: Always 0.
 */
int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			/* Child process */
			exit(0);
		}
		else if (child_pid > 0)
		{
			/* Parent process */
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
		{
			/* Error occurred */
			perror("fork");
			exit(1);
		}
	}
	infinite_while();
	return (0);
}
