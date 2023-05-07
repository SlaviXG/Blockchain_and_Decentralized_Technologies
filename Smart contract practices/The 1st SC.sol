pragma solidity 0.8.19;

contract HelloWorld {
   string public greet;

   constructor(string memory name) {
       require(bytes(name).length > 0, "name can't be empty");

       greet = string.concat("Hello world, hello ", name);
   }
}