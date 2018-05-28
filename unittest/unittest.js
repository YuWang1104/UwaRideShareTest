
function EmailErrorMessage({ isFilled, isValid }) {
  const show = isFilled && !isValid;
  if (show) {
    return (
      1
    );
  }
  return null;
}

//test EmailErrorMessage with four different inputs
test('EmailErrorMessage 1',function(){
	expect(EmailErrorMessage(true,false)).toBe(null);
});
test('EmailErrorMessage 2',function(){
	expect(EmailErrorMessage(true,true)).toBe(null);
});
test('EmailErrorMessage 3',function(){
	expect(EmailErrorMessage(false,false)).toBe(null);
});
test('EmailErrorMessage 3',function(){
	expect(EmailErrorMessage(false,true)).toBe(null);
});

