import { assertEquals } from "@std/assert";
import { add } from "./main.ts";

Deno.test(function addTest() {
  assertEquals(add(2, 3), 5);
});

Deno.test(function test(){
    assertEquals(add(3,3), 6);
})

Deno.test(function test(){
    assertEquals(add(3,4), 8);
})
