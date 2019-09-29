import styled from "styled-components/native";

export const Container = styled.View`
  flex: 1;
  align-items: center;
  justify-content: center;
  border: 1px solid blue;
`;

export const Place = styled.View`
  border: 1px solid red;
  margin: 5px 0px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: ${props => `${props.width}px`};
  height: 100px;
`;

export const Title = styled.Text`
  font-weight: 700;
  text-transform: uppercase;
`;

// export const ImagePlace = styled.Image`
//   width: 40%;
//   aspect-ratio: ${props => props.ratio};
// `;
