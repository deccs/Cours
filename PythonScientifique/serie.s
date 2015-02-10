	.file	"serie.C"
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.text
	.globl	_Z5seriedi
	.type	_Z5seriedi, @function
_Z5seriedi:
.LFB971:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movsd	%xmm0, -40(%rbp)
	movl	%edi, -44(%rbp)
	movq	-40(%rbp), %rax
	movq	%rax, -16(%rbp)
	movl	$0, %eax
	movq	%rax, -8(%rbp)
	movl	$1, -20(%rbp)
	jmp	.L2
.L3:
	cvtsi2sd	-20(%rbp), %xmm0
	movsd	-16(%rbp), %xmm1
	divsd	%xmm0, %xmm1
	movapd	%xmm1, %xmm0
	movsd	-8(%rbp), %xmm1
	addsd	%xmm1, %xmm0
	movsd	%xmm0, -8(%rbp)
	movsd	-16(%rbp), %xmm1
	movsd	.LC1(%rip), %xmm0
	xorpd	%xmm1, %xmm0
	mulsd	-40(%rbp), %xmm0
	movsd	%xmm0, -16(%rbp)
	addl	$1, -20(%rbp)
.L2:
	movl	-20(%rbp), %eax
	cmpl	-44(%rbp), %eax
	jle	.L3
	movq	-8(%rbp), %rax
	movq	%rax, -56(%rbp)
	movsd	-56(%rbp), %xmm0
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE971:
	.size	_Z5seriedi, .-_Z5seriedi
	.section	.rodata
.LC3:
	.string	"Calcul de la serie pour n="
.LC4:
	.string	" et x="
.LC5:
	.string	"Somme de la serie = "
.LC7:
	.string	"Log(1+x)="
	.text
	.globl	main
	.type	main, @function
main:
.LFB972:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$56, %rsp
	.cfi_offset 3, -24
	movl	%edi, -36(%rbp)
	movq	%rsi, -48(%rbp)
	movl	$20, -28(%rbp)
	movabsq	$4596373779694328218, %rax
	movq	%rax, -24(%rbp)
	movl	$.LC3, %esi
	movl	$_ZSt4cout, %edi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movl	-28(%rbp), %edx
	movl	%edx, %esi
	movq	%rax, %rdi
	call	_ZNSolsEi
	movl	$.LC4, %esi
	movq	%rax, %rdi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rax, %rdx
	movq	-24(%rbp), %rax
	movq	%rax, -56(%rbp)
	movsd	-56(%rbp), %xmm0
	movq	%rdx, %rdi
	call	_ZNSolsEd
	movl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_, %esi
	movq	%rax, %rdi
	call	_ZNSolsEPFRSoS_E
	movl	-28(%rbp), %edx
	movq	-24(%rbp), %rax
	movl	%edx, %edi
	movq	%rax, -56(%rbp)
	movsd	-56(%rbp), %xmm0
	call	_Z5seriedi
	movsd	%xmm0, -56(%rbp)
	movq	-56(%rbp), %rbx
	movl	$.LC5, %esi
	movl	$_ZSt4cout, %edi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rbx, -56(%rbp)
	movsd	-56(%rbp), %xmm0
	movq	%rax, %rdi
	call	_ZNSolsEd
	movl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_, %esi
	movq	%rax, %rdi
	call	_ZNSolsEPFRSoS_E
	movsd	-24(%rbp), %xmm1
	movsd	.LC6(%rip), %xmm0
	addsd	%xmm1, %xmm0
	call	log
	movsd	%xmm0, -56(%rbp)
	movq	-56(%rbp), %rbx
	movl	$.LC7, %esi
	movl	$_ZSt4cout, %edi
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rbx, -56(%rbp)
	movsd	-56(%rbp), %xmm0
	movq	%rax, %rdi
	call	_ZNSolsEd
	movl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_, %esi
	movq	%rax, %rdi
	call	_ZNSolsEPFRSoS_E
	movl	$0, %eax
	addq	$56, %rsp
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE972:
	.size	main, .-main
	.type	_Z41__static_initialization_and_destruction_0ii, @function
_Z41__static_initialization_and_destruction_0ii:
.LFB982:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movl	%esi, -8(%rbp)
	cmpl	$1, -4(%rbp)
	jne	.L7
	cmpl	$65535, -8(%rbp)
	jne	.L7
	movl	$_ZStL8__ioinit, %edi
	call	_ZNSt8ios_base4InitC1Ev
	movl	$__dso_handle, %edx
	movl	$_ZStL8__ioinit, %esi
	movl	$_ZNSt8ios_base4InitD1Ev, %edi
	call	__cxa_atexit
.L7:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE982:
	.size	_Z41__static_initialization_and_destruction_0ii, .-_Z41__static_initialization_and_destruction_0ii
	.type	_GLOBAL__sub_I__Z5seriedi, @function
_GLOBAL__sub_I__Z5seriedi:
.LFB983:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$65535, %esi
	movl	$1, %edi
	call	_Z41__static_initialization_and_destruction_0ii
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE983:
	.size	_GLOBAL__sub_I__Z5seriedi, .-_GLOBAL__sub_I__Z5seriedi
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I__Z5seriedi
	.section	.rodata
	.align 16
.LC1:
	.long	0
	.long	-2147483648
	.long	0
	.long	0
	.align 8
.LC6:
	.long	0
	.long	1072693248
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 4.8.2-19ubuntu1) 4.8.2"
	.section	.note.GNU-stack,"",@progbits
