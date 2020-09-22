#include <Python.h>
#include <stdio.h>

int isValidStr(const char *s);

/**
 * print_python_list - ?
 * @p: ?
 */
void print_python_list(PyObject *p)
{
	unsigned int size;
	unsigned int allocated;

	if (!PyList_Check(p))
		return;
	size = (unsigned int) PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	(void)p;
}

/**
 * print_python_bytes - ?
 * @p: ?
 */
void print_python_bytes(PyObject *p)
{
	unsigned int size;
	const char *str;
	unsigned int s_idx; /* str index */

	if (!PyBytes_Check(p))
		return;

	size = (unsigned int) PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %u\n", size);
	printf("  try string: ");

	str = PyBytes_AsString(p);

	if (isValidStr(str))
		printf("%s\n", str);
	else
		printf("??\n");

	printf("  first %d bytes: ", (size > 9) ? 10 : size + 1);
	for (s_idx = 0; s_idx < size + 1 && s_idx < 10; s_idx++)
	{
		printf("%02X", str[s_idx] & 0xFF);
		if (s_idx + 1 < size + 1 && s_idx + 1 < 10)
			putchar(' ');
		else
			putchar('\n');
	}
}

/**
 * print_python_float - ?
 * @p: ?
 */
void print_python_float(PyObject *p)
{
	(void) p;
}

/**
 * isValidStr - ?
 * @s: ?
 * Return: ?
 */
int isValidStr(const char *s)
{
	while (*s)
	{
		if (*s < ' ' || '~' < *s) /* revisar si no es desde 0 */
			return (0);
		s++;
	}
	return (1);
}