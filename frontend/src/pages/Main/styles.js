import styled from "styled-components/native";

export const Container = styled.View`
  flex: 1;
  align-items: center;
  justify-content: center;
`;

export const Place = styled.View`
  margin: 5px 0px;
  display: flex;
  justify-content: space-between;
  padding: 15px;
  align-items: center;
  width: ${props => `${props.width}px`};
  height: 100px;
  border: 1px dashed black;
`;

export const Title = styled.Text`
  font-weight: 400;
  text-transform: uppercase;
`;

export const Address = styled.Text`
  font-size: 12px;
`;

// export const ImagePlace = styled.Image`
//   width: 40%;
//   aspect-ratio: ${props => props.ratio};
// `;
