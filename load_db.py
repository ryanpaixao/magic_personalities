#!/usr/bin/env python
import sys
sys.path.append('.')
from app import db
from app import Questions

def load():
    question = Questions(None,sys.argv[1])
    # Insert a row of data
    db.session.add(question)
    # Save (commit) the changes
    db.session.commit()

if __name__ == "__main__":
    load()
