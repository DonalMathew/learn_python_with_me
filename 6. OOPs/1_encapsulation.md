### Consider **Chess-game**:


#### Case 1:

- Knight object:
```java
color="red";
```

If the user wants to see the color of the knight, it can be done by calling `knight.color` (i.e directly accessing data from the object).

##### Problem:
If the programmer working on knight object corrects the spelling of `color` to `colour`, then changes have to be made in the code, wherever the color was called.


#### Case 2 (Solution):

- Knight object:
```java
color="red";

public void getcolor(){
return color;
}
```

By setting a `getcolor()` and calling in it other places, will make sure that the data is not directly accessed by other methods, and changing `color` to `colour` inside this function will not need changes in elsewhere the property is called.