import React, { Component } from 'react';

export class InfoTable extends Component {

    render() {

        const TableHeaderRow = () => {
            return <tr><th>LongUrl</th><th>ShortUrl</th><th>Times clicked</th><th>created at</th></tr>;
        }

        const TableRow = ({ data }) => {
            return data.map((data) =>
                <tr key={data.id}>
                    <td>{data.longurl}</td><td>{data.shorturl}</td><td>{data.clicks}</td><td>{data.created_at}</td>
                </tr>
            );
        }

        const Table = ({ data }) => {
            return (
                <table>
                <tbody>
                    <TableHeaderRow />
                    <TableRow data={data} />
                </tbody>
                </table>
            );
        }


        return (
           < Table data={this.props.tableInfo}></Table>
        )
    }

}
export default InfoTable;