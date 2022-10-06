import argparse


class Context:
    _frame = 0
    _score = 0
    _fscore = 0
    _resultStr = ""
    _idx = 0
    _state = None
    _error = None
    _type_error = None

    @property
    def nextChar(self):
        if self._idx >= 0 and self._idx < len(self._resultStr):
            return self._resultStr[self._idx]
        else:
            return None

    def ToNextChar(self):
        self._idx += 1

    def __init__(self, resultStr: str) -> None:
        self._resultStr = resultStr
        self._idx = 0
        self.TransitionTo(StStart())

    def TransitionTo(self, state) -> None:
        self._state = state
        self._state.context = self
        print("Transition to {0}".format(state.__class__.__name__))

    def NextState(self) -> bool:
        self._state.Execute()
        return self._state.NextState()


class State:

    _context = None

    def Execute(self) -> None:
        pass

    def NextState(self) -> bool:
        return False

    def __str__(self) -> str:
        return "frame = {0}\nscore = {1}\nfscore = {2}\nidx = {3}\nnextChar = {4}" \
            .format(self.context._frame, self.context._score, self.context._fscore, \
                    self.context._idx, self.context.nextChar)

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @property
    def error(self) -> str:
        return self.context._error

    @error.setter
    def error(self, err) -> list:
        self.context._error = err[0]
        self.context._type_error = err[1]
        return self.context._error


class StateCharRead(State):
    def Execute(self) -> None:
        self.context.ToNextChar()
        return super().Execute()


class StStart(State):
    def Execute(self):
        return super().Execute()

    def NextState(self) -> bool:
        self.context.TransitionTo(StFinalizeFrame())
        return True


class StFinalizeFrame(State):
    def Execute(self):
        self.context._frame += 1
        self.context._score += self.context._fscore
        self.context._fscore = 0
        return super().Execute()

    def NextState(self) -> bool:

        if self.context._frame > 10:
            self.error = (f"Too many frames. Last score for {self.context._resultStr} is {self.context._score}",
                          "ValueError")
            self.context.TransitionTo(StErr())
            return True


        if None != self.context.nextChar:
            if 'X' == self.context.nextChar:
                self.context.TransitionTo(StX())
            elif '1' <= self.context.nextChar and '9' >= self.context.nextChar:
                self.context.TransitionTo(StDigit1())
            elif '-' == self.context.nextChar:
                self.context.TransitionTo(StMinus1())
            else:
                # TASK: make error message as StErr constructor argument
                self.error = ("Illegal symbol '{0}' after {1}" \
                    .format(self.context.nextChar, self.__class__.__name__), "ValueError")

                self.context.TransitionTo(StErr())
        else:
            self.context.TransitionTo(StEnd())
        return True


class StX(StateCharRead):
    def Execute(self):
        self.context._fscore = 20
        return super().Execute()

    def NextState(self) -> bool:
        self.context.TransitionTo(StFinalizeFrame())
        return True


class StDigit1(StateCharRead):
    def Execute(self) -> None:
        self.context._fscore = int(self.context.nextChar)
        return super().Execute()

    def NextState(self) -> bool:
        if None == self.context.nextChar:
            # TASK: make error message as StErr constructor argument
            self.error = "Illegal end after {0}" \
                .format(self.__class__.__name__)
            self.context.TransitionTo(StErr())
        elif '1' <= self.context.nextChar and '9' >= self.context.nextChar:
            self.context.TransitionTo(StDigit2())
        elif '/' == self.context.nextChar:
            self.context.TransitionTo(StSlash())
            pass
        elif '-' == self.context.nextChar:
            self.context.TransitionTo(StMinus2())
            pass
        else:
            # TASK: make error message as StErr constructor argument
            self.error = "Illegal symbol '{0}' after {1}" \
                .format(self.context.nextChar, self.__class__.__name__)
            self.context.TransitionTo(StErr())
        return True


class StDigit2(StateCharRead):
    def Execute(self) -> None:
        self.context._fscore += int(self.context.nextChar)
        return super().Execute()

    def NextState(self) -> bool:
        if self.context._fscore < 10:
            self.context.TransitionTo(StFinalizeFrame())
        else:
            self.error = "Illegal frame score '{0}' that is greater than the bowls count" \
                .format(self.context._fscore)
            self.context.TransitionTo(StErr())
        return True


class StMinus1(StateCharRead):
    def Execute(self) -> None:
        self.context._fscore = 0
        return super().Execute()

    def NextState(self) -> bool:
        if None == self.context.nextChar:
            # TASK: make error message as StErr constructor argument
            self.error = "Illegal end after {0}" \
                .format(self.__class__.__name__)
            self.context.TransitionTo(StErr())
        elif '1' <= self.context.nextChar and '9' >= self.context.nextChar:
            self.context.TransitionTo(StDigit2())
        elif '/' == self.context.nextChar:
            self.context.TransitionTo(StSlash())
            pass
        elif '-' == self.context.nextChar:
            self.context.TransitionTo(StMinus2())
            pass
        else:
            # TASK: make error message as StErr constructor argument
            self.error = "Illegal symbol '{0}' after {1}" \
                .format(self.context.nextChar, self.__class__.__name__)
            self.context.TransitionTo(StErr())
        return True


class StMinus2(StateCharRead):
    def Execute(self) -> None:
        return super().Execute()

    def NextState(self) -> bool:
        self.context.TransitionTo(StFinalizeFrame())
        return True


class StSlash(StateCharRead):
    def Execute(self) -> None:
        self.context._fscore = 15
        return super().Execute()

    def NextState(self) -> bool:
        self.context.TransitionTo(StFinalizeFrame())
        return True


class StErr(State):
    def Execute(self):
        if self.context._type_error == "ValueError":
            raise ValueError(self.context._error)




class StEnd(State):
    def Execute(self):
        print("Total score for '{0}' = {1}".format(self.context._resultStr, self.context._score))
        return super().Execute()

    def NextState(self) -> bool:
        return False


result = "XXXXXXXXXXX"

flContinue = True
ctx = Context(result)

while flContinue != False:
    flContinue = ctx.NextState()
