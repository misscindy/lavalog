//
//  NewBlockController.swift
//  lavalog
//
//  Created by Bingxin Fan on 6/10/18.
//  Copyright © 2018 Bingxin Fan. All rights reserved.
//

import UIKit
import GhostTypewriter

class NewBlockController: UIViewController {
    @IBOutlet weak var newBlockContent: UITextField!
    
    @IBOutlet weak var newBlockHint: TypewriterLabel!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        newBlockHint.textColor = UIColor.white.withAlphaComponent(0.5)
        
        newBlockHint.cancelTypewritingAnimation()
        newBlockHint.startTypewritingAnimation{ self.newBlockContent.becomeFirstResponder() }
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}

