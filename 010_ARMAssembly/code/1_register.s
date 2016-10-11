	.global _start
_start:
	@set a register
	MOV R0, #65

	@exit
	MOV R7, #1
	SWI 0
	

