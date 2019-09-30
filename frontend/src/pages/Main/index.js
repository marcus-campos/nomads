import React, { useState, useEffect } from "react";
import { FlatList, Dimensions, TouchableOpacity } from "react-native";
import { Rating } from "react-native-ratings";

import { Container, Place, Title, Address } from "./styles";

const Main = props => {
  const [places, setPlaces] = useState([]);

  useEffect(() => {
    async function loadPlaces() {
      const response = await fetch("http://localhost:3000/places");
      const data = await response.json();
      setPlaces(data);
    }
    loadPlaces();
  }, []);

  const handleClick = item => {
    return props.navigation.navigate("Detail", { item });
  };

  return (
    <Container>
      <FlatList
        contentContainerStyle={{ flexGrow: 1, justifyContent: "center" }}
        data={places}
        keyExtractor={place => String(place.id)}
        renderItem={({ item }) => (
          <TouchableOpacity onPress={() => handleClick(item)}>
            <Place width={Dimensions.get("window").width}>
              <Title>{item.name}</Title>
              <Rating
                type="star"
                readonly={true}
                ratingCount={5}
                imageSize={20}
                startingValue={item.score}
              />
              <Address>
                {item.address.city} - {item.address.state} . {item.phone}
              </Address>
            </Place>
          </TouchableOpacity>
        )}
      />
    </Container>
  );
};

export default Main;
