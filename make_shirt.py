def make_shirt(side, size='large', text='i love python'):
	print(f"you are ordering a {size} shirt, with '{text}' printed on the {side}.")

make_shirt('front','large','supreme')
make_shirt(size='large',side='right sleeve',text='lost but not forgotten')
make_shirt('back')
make_shirt('back','medium')