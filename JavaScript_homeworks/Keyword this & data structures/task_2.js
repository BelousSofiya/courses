//The product() function finds the product of an arbitrary number of arguments. You must specify the desired execution
//context for the product() function by implementing a new getProduct() function bound to the context of the object,
//which takes 2 additional arguments.
//The value of the 1st additional parameter is 2, the value of the 2nd additional parameter is 3. The object in the
//context of which the product() function is called has 1 property.

const product = function() {
    return [].reduce.call(arguments, function(res, elem) {
      return res * elem;
    }, this.product);
};

const contextObj = {'product': 20};// your code }

const getProduct = product.bind(contextObj, (2, 3));// product function that is called in the context of an contextObj
                     // with two additional parameters

//Tests

console.log(getProduct(4, 5));//Expect 1200

console.log(getProduct(6, 7));//Expect 2520

console.log(getProduct(0, 7));//Expect 0

console.log(getProduct(6, 0));//Expect 0

console.log(getProduct(-5, 5));//Expect -1500
