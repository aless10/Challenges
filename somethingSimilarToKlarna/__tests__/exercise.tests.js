import { shiftedDiff } from "../exercise_1";
import { describe, it } from "@jest/globals";

describe("shiftedDiff", () => {
  it("should work on basic tests", () => {
    assert.equal(shiftedDiff("eecoff", "coffee"), 4);
    assert.equal(shiftedDiff("Moose", "moose"), -1);
    assert.equal(shiftedDiff("isn't", "'tisn"), 2);
    assert.equal(shiftedDiff("Esham", "Esham"), 0);
    assert.equal(shiftedDiff(" ", " "), 0);
    assert.equal(shiftedDiff("hoop", "pooh"), -1);
    assert.equal(shiftedDiff("  ", " "), -1);
  });
});

describe('Order Weights', function() {
  it('basic tests', function() {
    assert.equal(orderWeight("103 123 4444 99 2000"), "2000 103 123 4444 99")
    assert.equal(orderWeight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
  });
});

describe("Follow That Spy", function() {
  it('Should return the correct route', function() {
    assert.deepEqual(findRoutes([["MNL", "TAG"], ["CEB", "TAC"], ["TAG", "CEB"], ["TAC", "BOR"]]), "MNL, TAG, CEB, TAC, BOR");
    assert.deepEqual(findRoutes([["Chicago", "Winnipeg"], ["Halifax", "Montreal"], ["Montreal", "Toronto"], ["Toronto", "Chicago"], ["Winnipeg", "Seattle"]]), "Halifax, Montreal, Toronto, Chicago, Winnipeg, Seattle");
  });
});
