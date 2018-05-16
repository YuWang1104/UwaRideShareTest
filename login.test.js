import 'react-native';
import React from 'react';
import renderer from 'react-test-renderer';
import SignIn from 'SignIn.js';

test('Matches snapshot for login page', () => {
  const render = renderer.create(
    <SignIn />,
  ).toJSON();
  expect(render).toMatchSnapshot();
});
