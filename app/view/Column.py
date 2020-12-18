
class Column :
    def __init__(self, name, backend) :
        self.ColumnWidget = Widget.GetLabelFrame(Window, _Text=name)
        self.ColumnWidget.pack(side=LEFT, fill=BOTH, expand=1)

        self.FrameList = Widget.GetList(ColumnWidget)
        self.FrameList.pack(fill=BOTH, expand=1, padx=5, pady=10)
        self.FrameList.bind("<BackSpace>", deleteActive)
        self.FrameList.bind("<Delete>", deleteActive)
        # FrameList.bind("<Down>", _FocusDownToDo)

        self.MoveToButton = Widget.GetButton(ColumnWidget, _Text="In Progress", _Command=lambda: MoveForward(s_List[1]))
        self.MoveToButton.pack(side=BOTTOM, fill=X)

        self.Entry = Widget.GetEntry(ColumnWidget)
        self.Entry.pack(side=BOTTOM, fill=X)
        self.Entry.bind("<Return>", _AddToToDo)

    def setMoveToRight(self, column) :
        self.FrameList.bind("<Command-Right>", column.takeData(self.FrameList.get(ACTIVE))

    def setFocusRight(self, column) :
        self.FrameList.bind("<Right>", column.takeFocus))

    def setFocusLeft(self, column) :
        self.FrameList.bind("<Left>", column.takeFocus))

    def takeFocus(self) :
        self.ColumnWidget.focus()

    def takeData(data) :
        backend.onDataReceived(data)

    def deleteActive() :
        backend.delete(self.FrameList.get(ACTIVE))
