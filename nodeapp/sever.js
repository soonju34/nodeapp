const express = require('express');
const { Db } = require('mongodb');
const app = express();
const MongoClient = require('mongodb').MongoClient;
const methodOverride = require("method-override")

app.use(methodOverride('_method'))
app.use(express.urlencoded({extended:true}))
app.set('view engine', 'ejs');
app.use(express.static('public'));

MongoClient.connect('mongodb+srv://admin:qwer1234@cluster0.q5tgfvc.mongodb.net/?retryWrites=true&w=majority',function(err, client){
    if (err) return console.log(err);
    
    db = client.db('nodeapp');
    // db.collection('board').insertOne({id : 'test1',pass : '1234',_id : 100},function(err,result){
    //     console.log('저장완료');
    // })

    app.listen(3000, function(){ 
        console.log('웹서버 실행중입니다')
    })
})

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html')
    
})

app.use('/board', require('./routes/board.js'))
app.use('/gallery', require('./routes/gallery.js'))

app.get('/write', function(req, res){
    res.render('board/write.ejs')
    
})

app.post('/ok', function(req,res){
    db.collection('counter').findOne({name : 'bCounter'},function(err,result){
        var totalPost = result.totalRecord;

    
        db.collection('board').insertOne({_id : (totalPost+1), title : req.body.title, name : req.body.name, content : req.body.memo, wdate : req.body.wdate}, function(err, result){
            // 수정할떄는 $set : 변경  $inc : 더하기
            db.collection('counter').updateOne({name : 'bCounter'},{$inc : {totalRecord:1}},function(err,result){
                if (err) {return console.log(err)}
                res.redirect('/list');
            })
        //console.log(req.body);
        //res.send('전송완료')   // 반드시 존재해야한다.
        
        })
    })
});    


app.get('/list',function(req,res){   //sort 정렬 -1 : 내림차순, 1 : 올림차순
    db.collection('board').find().sort({"_id" : -1}).toArray(function(err, result){
        console.log(result)
        res.render('board/list.ejs',{rows : result})    
    })    
})

app.get('/detail/:id',function(req,res){
    db.collection('board').findOne({_id:parseInt(req.params.id)}, function(err,result){
        res.render('board/detail.ejs', {rows: result})
    //res.send('전송완료')
    });
});




app.get('/edit/:id',function(req,res){
    db.collection('board').findOne({_id:parseInt(req.params.id)},function(err, result){
       console.log(result);
        res.render('board/edit.ejs', {rows : result})
       // res.send('전송완료')
    })
    
});

app.put('/edit',function(req,res){
    db.collection('board').updateOne({_id : parseInt(req.body.id)},{$set :{title : req.body.title, name : req.body.name, content : req.body.memo, wdate : req.body.wdate}},function(){
        
        res.redirect('/list')
    });
});



