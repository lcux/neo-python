# -*- coding:utf-8 -*-
"""
Description:
    Issue Transaction
Usage:
    from neo.Core.TX.IssueTransaction import IssueTransaction
"""
from neo.Core.TX.Transaction import Transaction,TransactionType

import random


class IssueTransaction(Transaction):

    Nonce = None

    """docstring for IssueTransaction"""
    def __init__(self, *args, **kwargs):
        super(IssueTransaction, self).__init__(*args, **kwargs)
        self.Type = TransactionType.IssueTransaction  # 0x40


    def GetScriptHashesForVerifying(self):
        """Get ScriptHash From SignatureContract"""
        pass

    def DeserializeExclusiveData(self, reader):
        self.Type = TransactionType.IssueTransaction
        pass
#        reader.ReadUInt32()

    def SerializeExclusiveData(self, writer):
        pass
#        writer.WriteUInt32(self.Nonce)
