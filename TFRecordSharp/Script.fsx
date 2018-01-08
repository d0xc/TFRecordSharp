///////////////////////////////////////////////////////////////////////////////
/// tests
//////////////////////////////////////////////////////////////////////////////
#I "bin/Release"
#r "DotNetZip.dll"
#r "Google.Protobuf.dll"
#r "WikiPricesPB.dll"
<<<<<<< HEAD
#r "Parquet.dll"
#r "TFRecordSharp.dll"


=======
#r "TFRecordSharp.dll"

>>>>>>> 7ac4f9065a19eb04701a3f3ebe5bd0cbc70d079c
open System.Text

open D1100.Data

// test1
let testFilename = "test_raw_string.dat"
let rec1 = [ "merry xmas" ]
let mapToBytesFun = fun (s: string) -> Encoding.UTF8.GetBytes(s)
do rec1 |> TFRecord.WriteAllRecords mapToBytesFun testFilename

let mapFromBytesFun = fun (ba: byte[]) -> Encoding.UTF8.GetString(ba)
let rec1Restored = TFRecord.ReadAllRecords mapFromBytesFun testFilename
rec1 = rec1Restored

// test2
let testFilename2 = "test_raw_string2.dat"
let recs2 = ["merry xmas"; "&"; "a happy new year"]
do recs2 |> TFRecord.WriteAllRecords mapToBytesFun testFilename2

let recs2Restored = TFRecord.ReadAllRecords mapFromBytesFun testFilename2 |> List.rev
recs2 = recs2Restored

// test with zlib compression
let recsZlib = List.append ([ 1 .. 1024*1024 ] |> List.map (sprintf "%d very very very")) [ "merry"; "christmas"]
do recsZlib |> TFRecord.WriteAllRecords mapToBytesFun "test_large_string_no_zlib.dat"
do recsZlib |> TFRecord.WriteAllRecordsZlibCompressed mapToBytesFun "test_large_string_zlib.dat"

let recsZlibNoCompresionRestored = TFRecord.ReadAllRecords mapFromBytesFun "test_large_string_no_zlib.dat" |> List.rev
recsZlib = recsZlibNoCompresionRestored

let recsZlibRestored = TFRecord.ReadAllRecordsZlibCompressed mapFromBytesFun "test_large_string_zlib.dat" |> List.rev
recsZlib = recsZlibRestored

// protocol buffer tests
///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

open System.IO
open Ionic.Zip
open Google.Protobuf
<<<<<<< HEAD
open Parquet
open Parquet.Data
=======
>>>>>>> 7ac4f9065a19eb04701a3f3ebe5bd0cbc70d079c
open D1100.Data.Encoding

let scriptdir = __SOURCE_DIRECTORY__
let wikipricefile =  scriptdir + "/data/WIKI_PRICES_sample.zip"

let ParseDoubleOrNaN (lia: string[]) (posi: int) =
    match lia.[posi] |> System.Double.TryParse with
    | (true,x ) ->
        x
    | (false,_) ->
        let wholeString = lia |> String.concat ","
        printfn "warn: error parsing double in position %d:" posi
        printfn "\t%s" wholeString
        System.Double.NaN

type ProtoWikiPriceDay = {
    ts: int64
    lia: string[]
}

/// essentially ready for making a map or grouping by timestamp
let WikiPriceEODToProtoWikiPriceDay (wikipricepath:string) =
    let zf = ZipFile.Read(wikipricepath)
    let priceEntry = zf.Entries |> Seq.exactlyOne
    use zreader = priceEntry.OpenReader()
    use sr = new StreamReader(zreader)
    do sr.ReadLine() |> ignore // sluff the header
    let epoch0 = new System.DateTime(1970,1,1) // only creat obj once for date conv
    let rec loop acc =
        if sr.EndOfStream then
            acc
        else
            let li = sr.ReadLine()
            let lia = li.Split([|','|])
            let ts = System.DateTime.Parse(lia.[1]).Subtract(epoch0).TotalSeconds |> int64 // 1 date 1999-11-18
            { ts = ts; lia = lia} :: acc |> loop
    [] |> loop

/// like above, but as a seq so you can Seq.take 100000 for example
/// for testing with constrained memory
let WikiPriceEODToProtoWikiPriceDaySeq (wikipricepath:string) =
    let zf = ZipFile.Read(wikipricepath)
    let priceEntry = zf.Entries |> Seq.exactlyOne
    let epoch0 = new System.DateTime(1970,1,1) // only creat obj once for date conv
    seq {  use zreader = priceEntry.OpenReader()
           use sr = new StreamReader(zreader)
           do sr.ReadLine() |> ignore // sluff the header
           while not sr.EndOfStream do
            let lia = sr.ReadLine().Split([|','|])
            let ts = System.DateTime.Parse(lia.[1]).Subtract(epoch0).TotalSeconds |> int64 // 1 date 1999-11-18
            yield { ts = ts; lia = lia} }

<<<<<<< HEAD
///////////////////////////////////////////////////////////////////////////////
/// protocol buffer tests here
//////////////////////////////////////////////////////////////////////////////
=======

>>>>>>> 7ac4f9065a19eb04701a3f3ebe5bd0cbc70d079c
        
/// each PB is one row in the file
/// more efficient memory wise to creat the PB's because no
/// need to group, but may not be as efficient to deserialize
/// downstream
/// lets the PB use the default value if can't parse (should be 
/// somewhat smaller.
let ProtoWikiPriceDaysToWikiPBRow (os: ProtoWikiPriceDay seq) =
    os |> Seq.map ( fun o ->
            let wp = new WikiDailyOHLCV()
            wp.Ticker <- o.lia.[0] // 0 ticker A
            wp.Ts <- o.ts
            do match o.lia.[2] |> System.Double.TryParse with
               | (true,x ) -> wp.Open <- x 
               | (false,_) -> ()
            match o.lia.[3] |> System.Double.TryParse with
               | (true,x ) -> wp.High <- x 
               | (false,_) -> ()
            match o.lia.[4] |> System.Double.TryParse with
               | (true,x ) -> wp.Low <- x 
               | (false,_) -> ()
            match o.lia.[5] |> System.Double.TryParse with
               | (true,x ) -> wp.Close <- x 
               | (false,_) -> ()
            match o.lia.[6] |> System.Double.TryParse with
               | (true,x ) -> wp.Volume <- x 
               | (false,_) -> ()
            match o.lia.[7] |> System.Double.TryParse with
               | (true,x ) -> wp.ExDividend <- x 
               | (false,_) -> ()
            match o.lia.[8] |> System.Double.TryParse with
               | (true,x ) -> wp.SplitRatio <- x 
               | (false,_) -> ()
            match o.lia.[9] |> System.Double.TryParse with
               | (true,x ) -> wp.AdjOpen <- x 
               | (false,_) -> ()
            match o.lia.[10] |> System.Double.TryParse with
               | (true,x ) -> wp.AdjHigh <- x 
               | (false,_) -> ()
            match o.lia.[11] |> System.Double.TryParse with
               | (true,x ) -> wp.AdjLow <- x 
               | (false,_) -> ()
            match o.lia.[12] |> System.Double.TryParse with
               | (true,x ) -> wp.AdjClose <- x 
               | (false,_) -> ()
            match o.lia.[13] |> System.Double.TryParse with
               | (true,x ) -> wp.AdjVolume <- x 
               | (false,_) -> ()
            wp)


/// first attempt at column wise using repeating fields to hold cols
let ProtoWikiPriceDaysToWikiDailyCol (oLst: (int64*ProtoWikiPriceDay list) list) =
    oLst
    |> List.map (
        fun (ts,os) ->
            let wp = new WikiDailyColOHLCV()
            wp.Dayts <- ts |> uint64
            for o in os do
                wp.Tickers.Add(o.lia.[0]) // 0 ticker A
                wp.Opens.Add(2 |> ParseDoubleOrNaN o.lia)
                wp.Highs.Add(3 |> ParseDoubleOrNaN o.lia)
                wp.Lows.Add(4 |> ParseDoubleOrNaN o.lia)
                wp.Closes.Add(5 |> ParseDoubleOrNaN o.lia)
                wp.Volumes.Add(6 |> ParseDoubleOrNaN o.lia)
                wp.ExDividends.Add(7 |> ParseDoubleOrNaN o.lia)
                wp.SplitRatios.Add(8 |> ParseDoubleOrNaN o.lia)
                wp.AdjOpens.Add(9 |> ParseDoubleOrNaN o.lia)
                wp.AdjHighs.Add(10 |> ParseDoubleOrNaN o.lia)
                wp.AdjLows.Add(11 |> ParseDoubleOrNaN o.lia)
                wp.AdjCloses.Add(12 |> ParseDoubleOrNaN o.lia)
                wp.AdjVolumes.Add(13 |> ParseDoubleOrNaN o.lia)
            wp)


/// second attempt at column wise using bytes field except for tickers
/// so wil require one more hop to fully deserialize
/// once you have n from tickers, then each field should have n = len / 8
/// doubles
let ProtoWikiPriceDaysToWikiDailyColBytes (oLst: (int64*ProtoWikiPriceDay list) list) =
    oLst
    |> List.map (
        fun (ts,os) ->
            let wp = new WikiDailyColBytesOHLCV()
            wp.Dayts <- ts |> uint64
            let tickers = [| for o in os -> o.lia.[0] |]
            let n = tickers.Length
            let opens = Array.zeroCreate<double> n
            let highs = Array.zeroCreate<double> n
            let lows = Array.zeroCreate<double> n
            let closes = Array.zeroCreate<double> n
            let volumes = Array.zeroCreate<double> n
            let exDividends = Array.zeroCreate<double> n
            let splitRatios = Array.zeroCreate<double> n
            let adjOpens = Array.zeroCreate<double> n
            let adjHighs = Array.zeroCreate<double> n
            let adjLows = Array.zeroCreate<double> n
            let adjCloses = Array.zeroCreate<double> n
            let adjVolumes = Array.zeroCreate<double> n
            os |> List.iteri (fun i o ->
                opens.[i] <- (2 |> ParseDoubleOrNaN o.lia)
                highs.[i] <- (3 |> ParseDoubleOrNaN o.lia)
                lows.[i] <- (4 |> ParseDoubleOrNaN o.lia)
                closes.[i] <- (5 |> ParseDoubleOrNaN o.lia)
                volumes.[i] <- (6 |> ParseDoubleOrNaN o.lia)
                exDividends.[i] <- (7 |> ParseDoubleOrNaN o.lia)
                splitRatios.[i] <- (8 |> ParseDoubleOrNaN o.lia)
                adjOpens.[i] <- (9 |> ParseDoubleOrNaN o.lia)
                adjHighs.[i] <- (10 |> ParseDoubleOrNaN o.lia)
                adjLows.[i] <- (11 |> ParseDoubleOrNaN o.lia)
                adjCloses.[i] <- (12 |> ParseDoubleOrNaN o.lia)
                adjVolumes.[i] <- (13 |> ParseDoubleOrNaN o.lia) )
            wp.Tickers.AddRange(tickers)
            wp.Opens <- ByteString.CopyFrom(opens |> EncodeDoubleArray)
            wp.Highs<- ByteString.CopyFrom(highs |> EncodeDoubleArray)
            wp.Lows<- ByteString.CopyFrom(lows |> EncodeDoubleArray)
            wp.Closes<- ByteString.CopyFrom(closes |> EncodeDoubleArray)
            wp.Volumes<- ByteString.CopyFrom(volumes |> EncodeDoubleArray)
            wp.ExDividends<- ByteString.CopyFrom(exDividends |> EncodeDoubleArray)
            wp.SplitRatios<- ByteString.CopyFrom(splitRatios |> EncodeDoubleArray)
            wp.AdjOpens<- ByteString.CopyFrom(adjOpens |> EncodeDoubleArray)
            wp.AdjHighs<- ByteString.CopyFrom(adjHighs |> EncodeDoubleArray)
            wp.AdjLows<- ByteString.CopyFrom(adjLows |> EncodeDoubleArray)
            wp.AdjCloses<- ByteString.CopyFrom(adjCloses |> EncodeDoubleArray)
            wp.AdjVolumes<- ByteString.CopyFrom(adjVolumes |> EncodeDoubleArray)
            wp)


///{ helper mapping funs
let mapPBToBytesFun = 
    fun pb -> MessageExtensions.ToByteString(pb).ToByteArray()

let mapBytesToColBytesPBFun = 
    fun (ba: byte[]) -> WikiDailyColBytesOHLCV.Parser.ParseFrom(ba)
let mapBytesToColPBFun = 
    fun (ba: byte[]) -> WikiDailyColOHLCV.Parser.ParseFrom(ba)
let mapBytesToPBFun = 
    fun (ba: byte[]) -> WikiDailyOHLCV.Parser.ParseFrom(ba)
///}

<<<<<<< HEAD
///////////////////////////////////////////////////////////////////////////////
/// parquet tests
///////////////////////////////////////////////////////////////////////////////

/// create a parquet DataSet
let ProtoWikiPriceDaysToWikiParquet (os: ProtoWikiPriceDay seq) =
    let ds = 
        new DataSet(    new DataField<string>("ticker"),
                        new DataField<int64>("ts"),
                        new DataField<double>("open"),
                        new DataField<double>("high"),
                        new DataField<double>("low"),
                        new DataField<double>("close"),
                        new DataField<double>("volume"),
                        new DataField<double>("exDividend"),
                        new DataField<double>("splitRatio"),
                        new DataField<double>("adjOpen"),
                        new DataField<double>("adjHigh"),
                        new DataField<double>("adjLow"),
                        new DataField<double>("adjClose"),
                        new DataField<double>("adjVolume"))
    for o in os do  
        ds.Add( o.lia.[0], // 0 ticker A
                o.ts,
                (2 |> ParseDoubleOrNaN o.lia), //opens.[i] <- 
                (3 |> ParseDoubleOrNaN o.lia), //highs.[i] <- 
                (4 |> ParseDoubleOrNaN o.lia), //lows.[i] <- 
                (5 |> ParseDoubleOrNaN o.lia), //closes
                (6 |> ParseDoubleOrNaN o.lia), //volumes
                (7 |> ParseDoubleOrNaN o.lia), //exDividends.[i] <-                 
                (8 |> ParseDoubleOrNaN o.lia), //splitRatios.[i] <- 
                (9 |> ParseDoubleOrNaN o.lia), //adjOpens.[i] <- 
                (10 |> ParseDoubleOrNaN o.lia), // adjHighs.[i] <- 
                (11 |> ParseDoubleOrNaN o.lia), //adjLows.[i] <- 
                (12 |> ParseDoubleOrNaN o.lia),      //adjCloses.[i] <- 
                (13 |> ParseDoubleOrNaN o.lia) ) //adjVolumes.[i] <-
    ds

//////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////
=======
>>>>>>> 7ac4f9065a19eb04701a3f3ebe5bd0cbc70d079c

// slurp up the whole file - takes a lot of memory
//let wpProtoPriceDay = wikipricefile |> WikiPriceEODToProtoWikiPriceDay

// total of  15188505 data rows
// out of memory so standardize on 1M
let wpProtoPriceDayLtd = 
    wikipricefile 
    |> WikiPriceEODToProtoWikiPriceDaySeq
    |> Seq.take 1000000


//34597.0 * 15.188505
//99773.0 * 15.188505

///////////////////////////////////////////////////////////////////////////////
// for testing columnular wikiprice using bytes for arrays
// for 1M lines got 102M bytes / 35M bytes

let wpcolbytes = 
    wpProtoPriceDayLtd
    |> List.ofSeq
    |> List.groupBy (fun o -> o.ts)
    |>  ProtoWikiPriceDaysToWikiDailyColBytes

let wpcolbytes1 = wpcolbytes |> List.head
do [wpcolbytes1] |> TFRecord.WriteAllRecords mapPBToBytesFun "test_wp_single_colbytespb_no_zlib.dat"
let wpcolbytes1NoZlibRestored = TFRecord.ReadAllRecords mapBytesToColBytesPBFun "test_wp_single_colbytespb_no_zlib.dat" |> Seq.exactlyOne
wpcolbytes1 = wpcolbytes1NoZlibRestored

do [wpcolbytes1] |> TFRecord.WriteAllRecordsZlibCompressed mapPBToBytesFun "test_wp_single_colbytespb_zlib.dat"
let wpcolbytes1ZlibRestored = TFRecord.ReadAllRecordsZlibCompressed mapBytesToColBytesPBFun "test_wp_single_colbytespb_zlib.dat" |> Seq.exactlyOne
wpcolbytes1 = wpcolbytes1ZlibRestored

///

do wpcolbytes |> TFRecord.WriteAllRecords mapPBToBytesFun "test_wp_all_colbytespb_no_zlib.dat"

do wpcolbytes |> TFRecord.WriteAllRecordsZlibCompressed mapPBToBytesFun "test_wp_all_colbytespb_zlib.dat"


///////////////////////////////////////////////////////////////////////////////
// for testing columnular wikiprice
// for 1M lines got 102M bytes / 35M bytes

let wpcols = 
    wpProtoPriceDayLtd
    |> List.ofSeq
    |> List.groupBy (fun o -> o.ts)
    |> ProtoWikiPriceDaysToWikiDailyCol 

let wpcol1 = wpcols |> Seq.head
do [wpcol1] |> TFRecord.WriteAllRecords mapPBToBytesFun "test_wp_single_colpb_no_zlib.dat"
let wpcolNoZlibRestored = TFRecord.ReadAllRecords mapBytesToColPBFun "test_wp_single_colpb_no_zlib.dat" |> Seq.exactlyOne
wpcol1 = wpcolNoZlibRestored

do [wpcol1] |> TFRecord.WriteAllRecordsZlibCompressed mapPBToBytesFun "test_wp_single_colpb_zlib.dat"
let wpcolZlibRestored = TFRecord.ReadAllRecordsZlibCompressed mapBytesToColPBFun "test_wp_single_colpb_zlib.dat" |> Seq.exactlyOne
wpcol1 = wpcolZlibRestored

///

do wpcols |> TFRecord.WriteAllRecords mapPBToBytesFun "test_wp_all_colpb_no_zlib.dat"

do wpcols |> TFRecord.WriteAllRecordsZlibCompressed mapPBToBytesFun "test_wp_all_colpb_zlib.dat"
  
///////////////////////////////////////////////////////////////////////////////
// for testing row by row pb
// for 1M rows got 126M bytes / 43M bytes

let wps = 
    wpProtoPriceDayLtd 
    |> ProtoWikiPriceDaysToWikiPBRow

let wp = wps |> Seq.head
do [wp] |> TFRecord.WriteAllRecords mapPBToBytesFun "test_wp_single_pb_no_zlib_ng.dat"
let wpNoZlibRestored = TFRecord.ReadAllRecords mapBytesToPBFun "test_wp_single_pb_no_zlib_ng.dat" |> Seq.exactlyOne
wp = wpNoZlibRestored

do [wp] |> TFRecord.WriteAllRecordsZlibCompressed mapPBToBytesFun "test_wp_single_pb_zlib_ng.dat"
let wpZlibRestored = TFRecord.ReadAllRecordsZlibCompressed mapBytesToPBFun "test_wp_single_pb_zlib_ng.dat" |> Seq.exactlyOne
wp = wpZlibRestored

///

do wps |> TFRecord.WriteAllRecords mapPBToBytesFun "test_wp_all_pb_no_zlib_1M.dat"

do wps |> TFRecord.WriteAllRecordsZlibCompressed mapPBToBytesFun "test_wp_all_pb_zlib_1M.dat"

<<<<<<< HEAD

///////////////////////////////////////////////////////////////////////////////
/// Parquet file tests
/// wow fast. uncompressed = 20 secs, compressed 21 secs
/// 109MB / 50MB compressed


let WriteDataSet (compression: Parquet.CompressionMethod) (filename:string) ds =
    use fs = new FileStream(filename,FileMode.Create,FileAccess.Write)
    do ParquetWriter.Write(ds, fs, compression)

// no compression
wpProtoPriceDayLtd 
|> ProtoWikiPriceDaysToWikiParquet 
|> WriteDataSet CompressionMethod.None "test_wp_all_pq_nocompress_1M.parquet"

// snappy
wpProtoPriceDayLtd 
|> ProtoWikiPriceDaysToWikiParquet 
|> WriteDataSet CompressionMethod.Snappy "test_wp_all_pq_snappy_1M.parquet"


=======
>>>>>>> 7ac4f9065a19eb04701a3f3ebe5bd0cbc70d079c
///////////////////////////////////////////////////////////////////////////////
// FYI just truncating the csv file I get
// for 1M rows 118M bytes / 27M bytes zipped






/////////////////////////////////////////////
// more simple unit tests
let foo = "merry xmas"
let fooUTF8Bytes = Encoding.UTF8.GetBytes(foo)
let packed = fooUTF8Bytes |> TFRecord.BytesToPacked
let len = match TFRecord.TryExtractLength packed.[0..7] packed.[8 .. 11] with | Some(i) -> i |> int32
let record = match TFRecord.TryExtractRecord packed.[12 .. (12 + len - 1)] packed.[(12 + len) ..] with | Some(ba) -> ba
foo = Encoding.UTF8.GetString(record)


    
