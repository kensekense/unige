//
//  Kripke+Extensions.swift
//  TP5
//
//  Created by Damien Morard on 13.11.18.
//

extension Kripke {

  public func pre(state_list: Set<String>) -> Set<String> {
    // Return the set of pre state
    // Ex: If we have: state = {"s0", "s1", "s2"}, trans = {("s0","s1"), ("s0", "s2")}
    // Then pre({"s1", "s2"}) = {"s0"}
    var new_state_list: Set<String> = []
    for transition in self.transitions {
      // transition[0]: from
      // transition[1]: to
      // Ex: (s0, s1) which means from s0 to s1
      if state_list.contains(where: {$0 == transition[1]}) {
        new_state_list.insert(transition[0])
      }
    }
    return new_state_list
  }

  public func compute(_ ctl_formula: CTL) -> Set<String> {
    // Compute a CTL formula and return a list of state
    // which verifiy CTL formula

    switch ctl_formula {

    case .ap(let x):
      var state_list: Set<String> = []
      for node in self.nodes {
        if node.value.contains(x) {
          state_list.insert(node.key)
        }
      }
      return state_list

    case .true:
      // TODO
      // return all the valid states
      var state_list: Set<String> = []
      for node in self.nodes {
        state_list.insert(node.key)
      }
      return state_list

    case .not(let x):
      // TODO
      // find all the valid states,
      // then subtract the states that contains x
      // return compute(.true).subtracting(compute(.ap(x)))
      return compute(.true).subtracting(compute(.reduce(x)))

    case .or(let x, let y):
      // TODO
      // find all the states that contains x, or y seperately,
      // then union their states
      return compute(.reduce(x)).union(compute(.reduce(y)))

    case .ex(let x):
      // TODO
      // [[EX x]] == preE([[x]])
      // [[x]], then preE([[x]])
      return pre(state_list: compute(.reduce(x)))

    case .ef(let x):
      // TODO
      // [[EF x]] == muY.[[x]] or preE[[Y]], muY for the least fixed point
      // [[x]], initilize Y as empty set of states due to muY
      let state_list4x = compute(.reduce(x))
      var Y: Set<String> = [] // initial Y

      var state_list: Set<String> = []
      var notfixedpoint = true // initial stop condition
      while notfixedpoint {
        state_list = state_list4x.union(pre(state_list: Y))
        // identify if it is fixed point
        if state_list == Y {
          notfixedpoint = false
        }
        else {
          Y = state_list
        }
      }

      return state_list

    case .eg(let x):
      // TODO
      // [[EG x]] == nuY.[[x]] and preE[[Y]], nuY for the greatest fixed point
      // [[x]], initilize Y as all possible states due to nuY
      let state_list4x = compute(.reduce(x))
      var Y: Set<String> = compute(.true) // initial Y

      var state_list: Set<String> = []
      var notfixedpoint = true // initial stop condition
      while notfixedpoint {
        state_list = state_list4x.intersection(pre(state_list: Y))
        // identify if it is fixed point
        if state_list == Y {
          notfixedpoint = false
        }
        else {
          Y = state_list
        }
      }

      return state_list

    case .eu(let x, let y):
      // TODO
      // [[x EU y]] == muY.[[y]] or ([[x]] and preE[[Y]])
      // [[x]] and [[y]], initilize Y as empty set of states due to muY
      let state_list4x = compute(.reduce(x))
      let state_list4y = compute(.reduce(y))
      var Y: Set<String> = [] // initial Y

      var state_list: Set<String> = []
      var notfixedpoint = true // initial stop condition
      while notfixedpoint {
        state_list = state_list4y.union(state_list4x.intersection(pre(state_list: Y)))
        // identify if it is fixed point
        if state_list == Y {
          notfixedpoint = false
        }
        else {
          Y = state_list
        }
      }

      return state_list

    // Don't touch the default value
    default: return []
    }

  }

}


extension Kripke: CustomStringConvertible {
  // Computed properties to have a nice print
  public var description: String {
    var string_nodes: String = ""
    var string_transitions: String = ""

    for node in nodes {
      string_nodes = "\(string_nodes)\n\(node.key): \(node.value)"
    }

    for transition in transitions {
      string_transitions = "\(string_transitions)\n\(transition[0]) -> \(transition[1])"
    }

    return "\(string_nodes)\n\(string_transitions)"
  }
}
